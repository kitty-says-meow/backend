from rest_framework import serializers

from departments.serializers import DepartmentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'pgas_score', 'personal_score',
        )
        read_only_fields = fields


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
            'username', 'first_name', 'last_name',
        )
        read_only_fields = fields
