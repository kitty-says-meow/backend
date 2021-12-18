from django.db.models import Q
from django_filters import CharFilter
from django_filters.rest_framework import FilterSet


def username_length(queryset, name, value):
    if len(value) >= 3:
        return queryset.filter(
            Q(username__startswith=value) | Q(first_name__icontains=value) | Q(last_name__icontains=value))[:10]
    return queryset.none()


class UserFilter(FilterSet):
    user = CharFilter(required=True, method=username_length)
