from django_filters import rest_framework as filters
from fims_core.models import Company


class CompanyFilter(filters.FilterSet):
    created_at__gte = filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
    created_at__lte = filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = Company
        fields = {
            "name": ["icontains"],
            "city": ["icontains"],
            "state": ["icontains"],
            "comp_code": ["exact", "icontains"],
            "status": ["exact"],
            "country": ["exact"],
        }
