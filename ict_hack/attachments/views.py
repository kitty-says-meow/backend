from drf_spectacular.utils import extend_schema_view
from rest_framework.mixins import CreateModelMixin
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import GenericViewSet

from attachments.models import Image
from attachments.openapi import *
from attachments.serializers import ImageSerializer


@extend_schema_view(
    create=images_create_schema,
)
class ImageViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser,)
    queryset = Image.objects.all()
