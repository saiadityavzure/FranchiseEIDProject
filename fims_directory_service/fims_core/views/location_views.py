from rest_framework import generics
from core.views.base import BaseFilteredView
from fims_core.models.location import Location
from fims_core.serializers.location_serializer import LocationSerializer
from fims_core.filters.location_filter import LocationFilter


class LocationListCreateView(BaseFilteredView, generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filterset_class = LocationFilter

    search_fields = ["code", "name"]
    ordering_fields = ["id", "code", "name"]
    ordering = ["id"]


class LocationRetrieveUpdateView(BaseFilteredView, generics.RetrieveUpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filterset_class = LocationFilter
