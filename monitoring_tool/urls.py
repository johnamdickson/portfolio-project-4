from . import views
from django.urls import path

urlpatterns = [
    path("", views.EmissionHome.as_view(), name="home"),
    path("emissions/", views.EmissionList.as_view(), name="emissions"),
    path("emissions_checks/", views.EmissionChecks.as_view(),
         name="emission_checks"),
    path('<slug:slug>/', views.Emissions.as_view(), name='emission_detail'),
]
