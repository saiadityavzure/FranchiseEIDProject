import django_filters
from core.filters.base import BaseFilter
from fims_core.models.location import Location


class LocationFilter(BaseFilter):

    code = django_filters.CharFilter(
        field_name="code",
        lookup_expr="icontains"
    )

    name = django_filters.CharFilter(
        field_name="name",
        lookup_expr="icontains"
    )

    company = django_filters.NumberFilter(
        field_name="company_id"
    )

    class Meta:
        model = Location
        fields = [
            "code",
            "name",
            "company",
            "status",
            "created_from",
            "created_to",
            "updated_from",
            "updated_to",
        ]
