from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Emission


class EmissionList(generic.ListView):
    model = Emission
    queryset = Emission.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
