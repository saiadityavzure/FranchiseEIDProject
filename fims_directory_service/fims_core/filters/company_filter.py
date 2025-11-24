import django_filters
from core.filters.base import BaseFilter
from fims_core.models.company import Company


class CompanyFilter(BaseFilter):
    """
    Company filter inspired by CountryFilter pattern + BaseFilter.
    """

    # Text filters similar to CountryFilter style
    name = django_filters.CharFilter(
        field_name="name",
        lookup_expr="icontains"
    )

    comp_code = django_filters.CharFilter(
        field_name="comp_code",
        lookup_expr="iexact"
    )

    city = django_filters.CharFilter(
        field_name="city",
        lookup_expr="icontains"
    )

    state = django_filters.CharFilter(
        field_name="state",
        lookup_expr="icontains"
    )

    # Foreign key filter (in same style as continent filter in CountryFilter)
    country = django_filters.NumberFilter(
        field_name="country_id"
    )

    class Meta:
        model = Company
        fields = [
            "name",
            "comp_code",
            "city",
            "state",
            "country",
            "status",          # inherited from BaseFilter
            "created_from",    # inherited
            "created_to",      # inherited
        ]
