from rest_framework import generics
from core.views.base import BaseFilteredView
from fims_core.models import Country
from fims_core.serializers.country_serializer import CountrySerializer
from fims_core.filters.country_filter import CountryFilter

class CountryListCreateView(BaseFilteredView, generics.ListCreateAPIView):
    """
    List or create countries.
    Supports continent filtering, code/name search, and pagination.
    """
    queryset = Country.objects.select_related("continent").all()
    serializer_class = CountrySerializer
    filterset_class = CountryFilter
    search_fields = ["name", "code"]


class CountryDetailView(BaseFilteredView, generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single country.
    """
    queryset = Country.objects.select_related("continent").all()
    serializer_class = CountrySerializer
