from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from events.models import Event
from events.openapi import *
from events.serializers import EventSerializer


@extend_schema_view(
    create=events_create_schema,
    retrieve=events_retrieve_schema,
    list=events_list_schema,
)
class EventsViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category',)
