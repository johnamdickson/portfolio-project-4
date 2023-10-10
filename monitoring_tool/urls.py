from . import views
from django.urls import path

urlpatterns = [
    path("", views.Emission.as_view(), name="home"),
]
