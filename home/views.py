from django.views.generic import ListView
from django.shortcuts import render
from .models import trip

# Create your views here.

class ModelListView(ListView):
    model = trip
    template_name = "home.html"
    #html code (in templates) now iterates through "object_list" list.
    #So don't use custom list query name!


def detail(request, pk):
    return render(request, 'detail.html', {"A":trip.objects.get(pk = pk)})