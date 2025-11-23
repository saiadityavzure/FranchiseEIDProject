import django_filters
from fims_core.models import Country

class CountryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    code = django_filters.CharFilter(lookup_expr="iexact")
    continent = django_filters.NumberFilter(field_name="continent_id")

    class Meta:
        model = Country
        fields = ["name", "code", "continent"]
