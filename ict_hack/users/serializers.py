from rest_framework import serializers

from departments.serializers import DepartmentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
        read_only_fields = fields


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'departments'
        )
        read_only_fields = fields

    departments = DepartmentSerializer(many=True)
