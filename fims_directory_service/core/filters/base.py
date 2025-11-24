import django_filters


class BaseFilter(django_filters.FilterSet):
    """
    Shared filters for all models inheriting from BaseModel:
    - status (ENABLED / DISABLED)
    - created_at range
    - updated_at range
    """

    status = django_filters.CharFilter(
        field_name="status",
        lookup_expr="iexact"
    )

    created_from = django_filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="gte"
    )

    created_to = django_filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="lte"
    )

    updated_from = django_filters.DateTimeFilter(
        field_name="updated_at",
        lookup_expr="gte"
    )

    updated_to = django_filters.DateTimeFilter(
        field_name="updated_at",
        lookup_expr="lte"
    )
