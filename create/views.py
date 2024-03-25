from django.shortcuts import render
from django.views.generic.edit import CreateView
from home.models import trip
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
class trip(PermissionRequiredMixin, CreateView):
    permission_required='home.add_trip'
    model = trip
    template_name = "create.html"
    fields="__all__"
    success_url="/"
    
