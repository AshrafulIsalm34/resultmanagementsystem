from django.urls import path
from . import views

urlpatterns = [
    path('rsd/', views.add_result, name='add_result'),
    path('success/', views.success, name='success'),
]

