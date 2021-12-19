from drf_spectacular.extensions import OpenApiSerializerFieldExtension
from drf_spectacular.plumbing import build_basic_type
from drf_spectacular.types import OpenApiTypes
from rest_framework import serializers

from attachments.models import Image
from attachments.serializers import ImageSerializer


class ImageField(serializers.SlugRelatedField):
    def __init__(self, **kwargs):
        super().__init__(queryset=Image.objects.all(), slug_field='pk', **kwargs)

    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super().get_queryset()
        return queryset.filter(created_by=request.user)

    def to_representation(self, value):
        return ImageSerializer(value, context=self.context).data.get('file')


class ImageFieldFix(OpenApiSerializerFieldExtension):
    target_class = 'attachments.fields.ImageField'

    def map_serializer_field(self, auto_schema, direction):
        if direction == 'request':
            return build_basic_type(OpenApiTypes.INT)
        else:
            return build_basic_type(OpenApiTypes.URI)
