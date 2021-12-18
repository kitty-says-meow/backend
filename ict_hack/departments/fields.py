from drf_spectacular.extensions import OpenApiSerializerFieldExtension
from drf_spectacular.plumbing import build_basic_type, append_meta
from drf_spectacular.types import OpenApiTypes
from rest_framework import serializers

from departments.models import Department
from departments.serializers import DepartmentSerializer


class DepartmentField(serializers.SlugRelatedField):
    def __init__(self):
        super().__init__(queryset=Department.objects.all(), slug_field='pk')

    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super().get_queryset()
        return queryset.filter(owner=request.user)

    def to_representation(self, value):
        return DepartmentSerializer(value, context=self.context).data


class DepartmentFieldFix(OpenApiSerializerFieldExtension):
    target_class = 'departments.fields.DepartmentField'

    def map_serializer_field(self, auto_schema, direction):
        if direction == 'request':
            return build_basic_type(OpenApiTypes.INT)
        else:
            meta = auto_schema._get_serializer_field_meta(DepartmentSerializer, direction)
            component = auto_schema.resolve_serializer(DepartmentSerializer, direction)
            return append_meta(component.ref, meta) if component else None
