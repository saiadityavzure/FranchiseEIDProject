from rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from core.pagination.base import DefaultPagination


class BaseView(generics.GenericAPIView):
    """
    Base view for all endpoints.
    """
    permission_classes = [AllowAny]


class BaseFilteredView(BaseView):
    """
    Adds filtering, searching, ordering, and pagination support.
    """

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,  # <-- REQUIRED for ordering
    ]

    pagination_class = DefaultPagination

    # Defaults (override in child views)
    filterset_class = None
    filterset_fields = []
    search_fields = []
    ordering_fields = "__all__"      # Allow ordering on all fields unless overridden
    ordering = ["id"]                # Default stable ordering
