from rest_framework import serializers

from achievements.models import Achievement
from achievements.serializers import AchievementCreateSerializer
from departments.fields import DepartmentField
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'category', 'date_start', 'date_end', 'department', 'achievements')

    department = DepartmentField()
    achievements = AchievementCreateSerializer(many=True)

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
