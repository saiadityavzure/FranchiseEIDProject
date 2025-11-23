import django_filters
from fims_core.models import Continent

class ContinentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    code = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Continent
        fields = ["name", "code"]
