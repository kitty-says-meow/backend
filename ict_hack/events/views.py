from django_filters.rest_framework import DjangoFilterBackend
from djangorestframework_camel_case.parser import CamelCaseMultiPartParser
from drf_spectacular.utils import extend_schema_view
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from events.enums import EventStatus
from events.models import Event
from events.openapi import *
from events.serializers import EventSerializer, EventReportSerializer


class EventReportPermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.status == EventStatus.PENDING_REPORT and obj.department in request.user.departments.all()


class EventJoinPermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.status == EventStatus.ACCEPTED and request.user != obj.department.owner


@extend_schema_view(
    create=events_create_schema,
    retrieve=events_retrieve_schema,
    list=events_list_schema,
    my=events_report_schema,
    report=events_report_schema,
)
class EventsViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category',)

    def list(self, request, *args, **kwargs):
        self.queryset = super().get_queryset().filter(status=EventStatus.ACCEPTED)
        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=['GET'])
    def my(self, request, *args, **kwargs):
        self.queryset = super().get_queryset().filter(department__in=self.request.user.departments.all())
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['POST'], serializer_class=EventReportSerializer, permission_classes=[EventReportPermission],
            parser_classes=[CamelCaseMultiPartParser])
    def report(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        serializer.save()

        output_serializer = EventSerializer(instance, context=self.get_serializer_context())
        return Response(output_serializer.data, status=200)

    @action(detail=True, methods=['POST'], serializer_class=None)
    def join(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.participants.add(self.request.user)
        return Response(status=201)
