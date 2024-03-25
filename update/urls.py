from django.urls import path
from . import views

urlpatterns = [
    path('', views.update.as_view(), name='update'),
]
