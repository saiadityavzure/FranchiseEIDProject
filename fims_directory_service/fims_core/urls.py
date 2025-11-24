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

from fims_core.views.corp_admin_views import (
    CorpAdminListCreateView,
    CorpAdminRetrieveUpdateView,
)

from fims_core.views.loc_admin_views import (
    LocAdminListCreateView,
    LocAdminRetrieveUpdateView,
)

from fims_core.views.location_user_views import (
    LocationUserListCreateView,
    LocationUserRetrieveUpdateView,
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

    # Locations
    path("locations/", LocationListCreateView.as_view(), name="location-list-create"),
    path("locations/<int:pk>/", LocationRetrieveUpdateView.as_view(), name="location-detail-update"),

    # CorpAdmins
    path("corp-admins/", CorpAdminListCreateView.as_view(), name="corp-admin-list-create"),
    path("corp-admins/<int:pk>/", CorpAdminRetrieveUpdateView.as_view(), name="corp-admin-detail-update"),

    # LocAdmins
    path("loc-admins/", LocAdminListCreateView.as_view(), name="loc_admin_list_create"),
    path("loc-admins/<int:pk>/", LocAdminRetrieveUpdateView.as_view(), name="loc_admin_retrieve_update"),

    # LocationUsers
    path("location-users/", LocationUserListCreateView.as_view(), name="location_user_list_create"),
    path( "location-users/<int:pk>/", LocationUserRetrieveUpdateView.as_view(), name="location_user_retrieve_update"),

]