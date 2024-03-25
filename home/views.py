from django.shortcuts import render
from .models import trip

# Create your views here.

def home(request):
    return render(request, 'home.html',{"A":trip.objects.all()})

def detail(request, pk):
    return render(request, 'detail.html', {"A":trip.objects.get(pk = pk)})