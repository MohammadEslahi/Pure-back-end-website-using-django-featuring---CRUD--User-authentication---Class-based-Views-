from django.shortcuts import render
from django.views.generic.edit import UpdateView
from home.models import trip
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

class update(PermissionRequiredMixin, UpdateView):
    permission_required='home.change_trip'
    model = trip
    template_name = "update.html"
    fields='__all__'
    success_url="/"
    