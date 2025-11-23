from rest_framework import generics
from core.views.base import BaseFilteredView
from fims_core.models import Continent
from fims_core.serializers.continent_serializer import ContinentSerializer
from fims_core.filters.continent_filter import ContinentFilter

class ContinentListCreateView(BaseFilteredView, generics.ListCreateAPIView):
    """
    List all continents or create a new continent.
    Supports filtering, searching, and pagination.
    """
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer
    filterset_class = ContinentFilter
    search_fields = ["name", "code"]


class ContinentDetailView(BaseFilteredView, generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a continent.
    """
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer
