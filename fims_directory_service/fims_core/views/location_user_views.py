from rest_framework import generics
from core.views.base import BaseFilteredView
from fims_core.models.location_user import LocationUser
from fims_core.serializers.location_user_serializer import LocationUserSerializer
from fims_core.filters.location_user_filter import LocationUserFilter


class LocationUserListCreateView(BaseFilteredView, generics.ListCreateAPIView):
    """
    GET  /api/location-users/       -> list with filters/search/order
    POST /api/location-users/       -> create new location user
    """
    queryset = LocationUser.objects.select_related("company", "location")
    serializer_class = LocationUserSerializer
    filterset_class = LocationUserFilter

    search_fields = ["first_name", "last_name", "email"]
    ordering_fields = ["id", "first_name", "last_name", "email", "company_id", "location_id"]
    ordering = ["id"]


class LocationUserRetrieveUpdateView(BaseFilteredView, generics.RetrieveUpdateAPIView):
    """
    GET   /api/location-users/<id>/  -> fetch one
    PATCH /api/location-users/<id>/  -> partial update
    PUT   /api/location-users/<id>/  -> full update
    """
    queryset = LocationUser.objects.select_related("company", "location")
    serializer_class = LocationUserSerializer
    filterset_class = LocationUserFilter
