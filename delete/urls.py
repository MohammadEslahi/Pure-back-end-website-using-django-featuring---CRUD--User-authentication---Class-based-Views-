from django.urls import path
from . import views

urlpatterns = [
    path('', views.ModelDeleteView.as_view(), name='delete')
]
