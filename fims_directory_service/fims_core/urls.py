from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fims_core.views.company_view import (
    CompanyListCreateView,
    CompanyRetrieveUpdateView,
)

from fims_core.views.continent_views import (
    ContinentListCreateView,
    ContinentDetailView,
)
from fims_core.views.country_views import (
    CountryListCreateView,
    CountryDetailView,
)

from fims_core.views.location_views import (
    LocationListCreateView,
    LocationRetrieveUpdateView
)

urlpatterns = [
    # Continents
    path("continents/", ContinentListCreateView.as_view(), name="continent-list"),
    path("continents/<int:pk>/", ContinentDetailView.as_view(), name="continent-detail"),

    # Countries
    path("countries/", CountryListCreateView.as_view(), name="country-list"),
    path("countries/<int:pk>/", CountryDetailView.as_view(), name="country-detail"),

    # Companies
    path("companies/", CompanyListCreateView.as_view(), name="company-list-create"),
    path("companies/<int:pk>/", CompanyRetrieveUpdateView.as_view(), name="company-detail-update"),

    path("locations/", LocationListCreateView.as_view(), name="location-list-create"),
    path("locations/<int:pk>/", LocationRetrieveUpdateView.as_view(), name="location-detail-update"),

]