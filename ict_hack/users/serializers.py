from rest_framework import serializers

from achievements.serializers import UserAchievementSerializer
from departments.serializers import DepartmentSerializer
from trophies.serializers import TrophySerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'avatar', 'pgas_score', 'personal_score', 'achievements', 'trophies',
        )
        read_only_fields = fields

    achievements = UserAchievementSerializer(many=True, source='achievements_confirmed')
    trophies = TrophySerializer(many=True)


class ProfileSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + (
            'email', 'departments',
        )
        read_only_fields = fields

    departments = DepartmentSerializer(many=True)


class ScoreOperationSerializer(serializers.Serializer):
    score = serializers.IntegerField(min_value=1)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'pgas_score',
        )
        read_only_fields = fields


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'avatar'
        )
        read_only_fields = fields
