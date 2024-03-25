from django.shortcuts import render
from django.views.generic.edit import DeleteView
# Create your views here.
from home.models import trip
from django.contrib.auth.mixins import PermissionRequiredMixin

class ModelDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required=('home.delete_trip')
    model = trip
    template_name = "confirmdelete.html"
    success_url='/'