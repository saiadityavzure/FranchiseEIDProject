import django_filters
from core.filters.base import BaseFilter
from fims_core.models.loc_admin import LocAdmin


class LocAdminFilter(BaseFilter):
    """
    Filtering support for Location Admins.
    Inherits:
      - status
      - created_at range
      - updated_at range
    Custom filters:
      - first_name, last_name (icontains)
      - email (icontains)
      - company_id (exact)
      - location_id (exact)
    """

    first_name = django_filters.CharFilter(
        field_name="first_name",
        lookup_expr="icontains"
    )

    last_name = django_filters.CharFilter(
        field_name="last_name",
        lookup_expr="icontains"
    )

    email = django_filters.CharFilter(
        field_name="email",
        lookup_expr="icontains"
    )

    company = django_filters.NumberFilter(
        field_name="company_id"
    )

    location = django_filters.NumberFilter(
        field_name="location_id"
    )

    class Meta:
        model = LocAdmin
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
