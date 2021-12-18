from django.db import IntegrityError, transaction
from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.filters import UserFilter
from users.models import User
from users.openapi import *
from users.serializers import ProfileSerializer, UserSerializer, ScoreOperationSerializer


class ProfilePermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user == obj


@extend_schema_view(
    retrieve=users_profile_schema,
    profile=users_profile_schema,
    search=users_search_schema,
    score_convert=users_score_convert_schema,
    score_send=users_score_send_schema,
)
class UsersViewSet(GenericViewSet, RetrieveModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    filterset_class = UserFilter

    @action(detail=False, methods=['GET'], filter_backends=(DjangoFilterBackend,))
    def search(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'], serializer_class=ProfileSerializer, permission_classes=[ProfilePermission])
    def profile(self, request, *args, **kwargs):
        self.kwargs['username'] = self.request.user.username
        return super().retrieve(request, *args, **self.kwargs)

    @action(detail=False, methods=['POST'], serializer_class=ScoreOperationSerializer, permission_classes=[ProfilePermission],
            url_path='score/convert')
    def score_convert(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user.pgas_score = F('pgas_score') - serializer.validated_data['score']
            user.personal_score = F('personal_score') + serializer.validated_data['score']
            user.save()
        except IntegrityError:
            raise ValidationError({'score': 'Недостаточно средств.'})
        else:
            return Response(status=200)

    @action(detail=True, methods=['POST'], serializer_class=ScoreOperationSerializer, url_path='score/send')
    def score_send(self, request, *args, **kwargs):
        user_from = self.request.user
        user_to = self.get_object()

        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        try:
            with transaction.atomic():
                user_from.personal_score = F('personal_score') - serializer.validated_data['score']
                user_to.personal_score = F('personal_score') + serializer.validated_data['score']
                user_from.save()
                user_to.save()

        except IntegrityError:
            raise ValidationError({'score': 'Недостаточно средств.'})
        else:
            return Response(status=200)
