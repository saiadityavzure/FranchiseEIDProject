from django_filters import rest_framework as filters


class BaseFilterSet(filters.FilterSet):
    created_at__gte = filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
    created_at__lte = filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")
    status = filters.CharFilter(field_name="status", lookup_expr="iexact")
