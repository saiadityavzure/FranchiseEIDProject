from rest_framework import generics
from core.views.base import BaseFilteredView
from fims_core.models import Company
from fims_core.serializers.company_serializer import CompanySerializer
from fims_core.filters.company_filters import CompanyFilter


class CompanyListCreateView(BaseFilteredView, generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    filterset_class = CompanyFilter
    search_fields = ["name", "city", "state", "comp_code"]

    ordering_fields = [
        "name",
        "city",
        "created_at",
        "updated_at",
        "status",
        "comp_code",
    ]
    ordering = ["-created_at"]

    def get_queryset(self):
        # Return non-deleted rows (if soft delete added later)
        return Company.objects.all()


class CompanyDetailView(BaseFilteredView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer