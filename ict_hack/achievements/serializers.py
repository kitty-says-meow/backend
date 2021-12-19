from typing import Union

from django.utils.functional import classproperty
from rest_framework import serializers

from achievements.models import Achievement


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'name', 'score', 'user')

        @classproperty
        def read_only_fields(cls):
            writable_fields = ('name', 'score',)
            return list(filter(lambda field: field not in writable_fields, cls.fields))

    user = serializers.SlugRelatedField(slug_field='username', read_only=True)


class UserAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = (
            'id', 'name', 'score', 'event', 'category', 'image'
        )
        read_only_fields = fields

    event = serializers.ReadOnlyField(source='event.name')
    category = serializers.ReadOnlyField(source='event.category')
    image = serializers.SerializerMethodField()

    # image = serializers.ImageField(source='event.image', read_only=True)

    def get_image(self, obj) -> Union[None, str]:
        return None
