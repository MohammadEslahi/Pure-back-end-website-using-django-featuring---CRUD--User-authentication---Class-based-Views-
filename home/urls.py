from django.urls import path
from . import views


urlpatterns = [
    path('', views.ModelListView.as_view(), name='home'),
    path('<int:pk>/', views.detail, name='detail'),
]
