from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fims_core.views.company_view import (
    CompanyListCreateView,
    CompanyDetailView,
)

from fims_core.views.continent_views import (
    ContinentListCreateView,
    ContinentDetailView,
)
from fims_core.views.country_views import (
    CountryListCreateView,
    CountryDetailView,
)

urlpatterns = [
    # Continents
    path("continents/", ContinentListCreateView.as_view(), name="continent-list"),
    path("continents/<int:pk>/", ContinentDetailView.as_view(), name="continent-detail"),

    # Countries
    path("countries/", CountryListCreateView.as_view(), name="country-list"),
    path("countries/<int:pk>/", CountryDetailView.as_view(), name="country-detail"),

    # Companies
    path("companies/", CompanyListCreateView.as_view(), name="companies-list-create"),
    path("companies/<int:pk>/", CompanyDetailView.as_view(), name="companies-detail"),

]