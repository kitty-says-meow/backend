from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from achievements.models import Achievement
from achievements.serializers import AchievementSerializer
from attachments.fields import ImageField
from departments.fields import DepartmentField
from events.enums import EventStatus
from events.models import Event
from users.models import User
from users.serializers import ParticipantSerializer


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id', 'name', 'description', 'category', 'date_start', 'date_end', 'department', 'image', 'report', 'status',
            'achievements', 'participants',
        )
        read_only_fields = ('report', 'status')

    department = DepartmentField()
    image = ImageField(required=False, allow_null=True)
    achievements = AchievementSerializer(many=True, allow_empty=False)
    participants = ParticipantSerializer(many=True, read_only=True)

    def validate(self, attrs):
        date_start, date_end = attrs.get('date_start'), attrs.get('date_end')
        if not (date_start and date_end):
            attrs['date_start'], attrs['date_end'] = None, None
        return attrs

    def create(self, validated_data):
        achievements_data = validated_data.pop('achievements', [])

        instance = super().create(validated_data)

        if not (instance.date_start and instance.date_end):
            instance.status = EventStatus.PENDING_REPORT
            instance.save()

        achievements = [Achievement(event=instance, **item) for item in achievements_data]
        Achievement.objects.bulk_create(achievements)

        return instance


class EventReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('report', 'users',)

    report = serializers.FileField(required=True, allow_null=False)
    users = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', many=True)

    def update(self, instance, validated_data):
        achievements = instance.achievements.all().order_by('id')
        users = validated_data.pop('users', None)
        if not (users is not None and len(users) == achievements.count()):
            raise ValidationError({'users': 'Количество пользователей должно совпадать с количеством достижений.'})

        for user, achievement in zip(users, achievements):
            achievement.user = user

        Achievement.objects.bulk_update(achievements, ['user'])

        validated_data['status'] = EventStatus.PENDING_REPORT_CONFIRMATION

        return super().update(instance, validated_data)
