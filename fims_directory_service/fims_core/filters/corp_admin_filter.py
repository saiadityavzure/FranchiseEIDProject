import django_filters
from core.filters.base import BaseFilter
from fims_core.models.corp_admin import CorpAdmin


class CorpAdminFilter(BaseFilter):
    first_name = django_filters.CharFilter(field_name="first_name", lookup_expr="icontains")
    last_name = django_filters.CharFilter(field_name="last_name", lookup_expr="icontains")
    email = django_filters.CharFilter(field_name="email", lookup_expr="icontains")
    company = django_filters.NumberFilter(field_name="company_id")

    class Meta:
        model = CorpAdmin
        fields = [
            "first_name",
            "last_name",
            "email",
            "company",
            "status",
            "created_from",
            "created_to",
            "updated_from",
            "updated_to",
        ]
