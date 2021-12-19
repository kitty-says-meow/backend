from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from achievements.models import Achievement
from achievements.serializers import AchievementSerializer
from departments.fields import DepartmentField
from events.enums import EventStatus
from events.models import Event
from users.models import User


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id', 'name', 'description', 'category', 'date_start', 'date_end', 'department', 'report', 'status', 'achievements'
        )

    department = DepartmentField()
    achievements = AchievementSerializer(many=True)

    def validate(self, attrs):
        date_start, date_end = attrs.get('date_start'), attrs.get('date_end')
        if not (date_start and date_end):
            attrs['date_start'], attrs['date_end'] = None, None
        return attrs

    def create(self, validated_data):
        achievements_data = validated_data.pop('achievements', [])
        instance = super().create(validated_data)
        achievements = [Achievement(event=instance, **item) for item in achievements_data]
        Achievement.objects.bulk_create(achievements)
        return instance


class EventReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('report', 'users',)

    users = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', many=True)

    def update(self, instance, validated_data):
        achievements = instance.achievements.all()
        users = validated_data.pop('users', None)
        if not (users is not None and len(users) == achievements.count()):
            raise ValidationError({'users': 'Количество пользователей должно совпадать с количеством достижений.'})

        for user, achievement in zip(users, achievements):
            achievement.user = user

        Achievement.objects.bulk_update(achievements, ['user'])

        validated_data['status'] = EventStatus.PENDING_REPORT_CONFIRMATION

        return super().update(instance, validated_data)
