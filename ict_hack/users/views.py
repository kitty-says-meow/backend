from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from users.filters import UserFilter
from users.models import User
from users.openapi import *
from users.serializers import ProfileSerializer, UserSerializer


class ProfilePermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user == obj


@extend_schema_view(
    get=profile_get_schema,
)
class ProfileView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (ProfilePermission,)

    queryset = User.objects.all()

    def get_queryset(self):
        return self.get_object()

    def get_object(self):
        return self.request.user


@extend_schema_view(
    get=users_search_get_schema,
)
class UsersSearchView(ListAPIView):
    queryset = User.objects.all()

    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter
