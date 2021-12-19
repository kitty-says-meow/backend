from django.utils.functional import classproperty
from rest_framework import serializers

from achievements.models import Achievement
from events.models import Event


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'name', 'score', 'user')

        @classproperty
        def read_only_fields(cls):
            writable_fields = ('name', 'score',)
            return list(filter(lambda field: field not in writable_fields, cls.fields))

    user = serializers.SlugRelatedField(slug_field='username', read_only=True)


class UserAchievementEvent(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'category', 'image')
        read_only_fields = fields


class UserAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = (
            'id', 'name', 'score', 'event'
        )
        read_only_fields = fields

    event = UserAchievementEvent(read_only=True)


class AchievementRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = (
            'id', 'user', 'score', 'pgas_converted'
        )
        read_only_fields = fields

    user = serializers.ReadOnlyField(source='user.username')
