from django.urls import path
from . import views


urlpatterns = [
    path('', views.trip.as_view() , name='create')
]
