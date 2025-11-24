import django_filters
from core.filters.base import BaseFilter
from fims_core.models.location_user import LocationUser


class LocationUserFilter(BaseFilter):
    """
    Filtering for Location Users.

    Inherits BaseFilter:
      - status
      - created_from / created_to
      - updated_from / updated_to
    """

    first_name = django_filters.CharFilter(
        field_name="first_name",
        lookup_expr="icontains",
    )
    last_name = django_filters.CharFilter(
        field_name="last_name",
        lookup_expr="icontains",
    )
    email = django_filters.CharFilter(
        field_name="email",
        lookup_expr="icontains",
    )

    company = django_filters.NumberFilter(field_name="company_id")
    location = django_filters.NumberFilter(field_name="location_id")

    class Meta:
        model = LocationUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "company",
            "location",
            "status",
            "created_from",
            "created_to",
            "updated_from",
            "updated_to",
        ]
