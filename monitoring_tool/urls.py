from . import views
from django.urls import path

urlpatterns = [
    path("", views.EmissionList.as_view(), name="home"),
    path("emissions/", views.Emissions.as_view(), name="emissions"),
    path("emissions_checks/", views.EmissionChecks.as_view(), name="emission_checks"),
]
