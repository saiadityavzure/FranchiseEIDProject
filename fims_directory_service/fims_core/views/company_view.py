from rest_framework import generics
from core.views.base import BaseFilteredView
from fims_core.models.company import Company
from fims_core.serializers.company_serializer import CompanySerializer
from fims_core.filters.company_filter import CompanyFilter


class CompanyListCreateView(BaseFilteredView, generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filterset_class = CompanyFilter
    search_fields = ["name", "city", "state", "comp_code"]
    ordering_fields = ["id", "name", "city", "state", "comp_code"]
    ordering = ["id"]


class CompanyRetrieveUpdateView(BaseFilteredView, generics.RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filterset_class = CompanyFilter
