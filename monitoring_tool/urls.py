from . import views
from django.urls import path

urlpatterns = [
    path("", views.EmissionHome.as_view(), name="home"),
    path("emissions/", views.EmissionList.as_view(), name="emissions"),
    path("emission_checks/", views.EmissionCheckList.as_view(),
         name="emission_checks"),
    path('add-emission/', views.addEmission, name="add-emission"),
    path('close-emission/<slug:slug>/', views.Emissions.close, name="close-emission"),
    path('delete-emission/<slug:slug>/', views.Emissions.delete, name="delete-emission"),
    path('<slug:slug>/', views.Emissions.as_view(), name='emission_detail'),
    path('add-check/<slug:slug>/', views.addCheck, name="add-check"),
    path('delete-check/<slug:slug>/<int:id>', views.deleteCheck, name="delete-check"),
]
