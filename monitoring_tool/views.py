from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Emission, EmissionCheck


class EmissionList(generic.ListView):
    model = Emission
    queryset = Emission.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class Emissions(generic.ListView):
    model = Emission
    queryset = Emission.objects.filter(status=1).order_by("-created_on")
    template_name = "emission.html"
    paginate_by = 6


class EmissionChecks(generic.ListView):
    model = EmissionCheck
    queryset = EmissionCheck.objects.filter(status=1).order_by("-date_checked")
    template_name = "emission_checks.html"
    paginate_by = 6
