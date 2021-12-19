from django.utils.functional import classproperty
from rest_framework import serializers

from achievements.models import Achievement
from users.models import User


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'name', 'score', 'user')

        @classproperty
        def read_only_fields(cls):
            writable_fields = ('name', 'score',)
            return list(filter(lambda field: field not in writable_fields, cls.fields))

    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
