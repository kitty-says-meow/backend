from django.utils.functional import classproperty
from rest_framework import serializers

from achievements.models import Achievement


class AchievementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'name', 'score', 'user')

        @classproperty
        def read_only_fields(cls):
            writable_fields = ('name', 'score',)
            return list(filter(lambda field: field not in writable_fields, cls.fields))


class AchievementUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'name', 'score', 'user')

        @classproperty
        def read_only_fields(cls):
            writable_fields = ('user',)
            return list(filter(lambda field: field not in writable_fields, cls.fields))
