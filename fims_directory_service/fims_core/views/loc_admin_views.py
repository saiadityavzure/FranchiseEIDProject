from rest_framework import generics
from core.views.base import BaseFilteredView
from fims_core.models.loc_admin import LocAdmin
from fims_core.serializers.loc_admin_serializer import LocAdminSerializer
from fims_core.filters.loc_admin_filter import LocAdminFilter


class LocAdminListCreateView(BaseFilteredView, generics.ListCreateAPIView):
    """
    GET  /api/loc-admins/     -> list with filtering/search/order
    POST /api/loc-admins/     -> create new location admin
    """
    queryset = LocAdmin.objects.select_related("company", "location")
    serializer_class = LocAdminSerializer
    filterset_class = LocAdminFilter

    # Searchable fields
    search_fields = ["first_name", "last_name", "email"]

    # Fields allowed to order by
    ordering_fields = ["id", "first_name", "last_name", "email", "company_id", "location_id"]

    # Default ordering
    ordering = ["id"]


class LocAdminRetrieveUpdateView(BaseFilteredView, generics.RetrieveUpdateAPIView):
    """
    GET    /api/loc-admins/<id>/   -> fetch one
    PATCH  /api/loc-admins/<id>/   -> update partial
    PUT    /api/loc-admins/<id>/   -> update full
    """
    queryset = LocAdmin.objects.select_related("company", "location")
    serializer_class = LocAdminSerializer
    filterset_class = LocAdminFilter
