from rest_framework import generics
from core.views.base import BaseFilteredView
from fims_core.models.corp_admin import CorpAdmin
from fims_core.serializers.corp_admin_serializer import CorpAdminSerializer
from fims_core.filters.corp_admin_filter import CorpAdminFilter


class CorpAdminListCreateView(BaseFilteredView, generics.ListCreateAPIView):
    queryset = CorpAdmin.objects.all()
    serializer_class = CorpAdminSerializer
    filterset_class = CorpAdminFilter

    search_fields = ["first_name", "last_name", "email"]
    ordering_fields = ["id", "first_name", "last_name", "email"]
    ordering = ["id"]


class CorpAdminRetrieveUpdateView(BaseFilteredView, generics.RetrieveUpdateAPIView):
    queryset = CorpAdmin.objects.all()
    serializer_class = CorpAdminSerializer
    filterset_class = CorpAdminFilter
