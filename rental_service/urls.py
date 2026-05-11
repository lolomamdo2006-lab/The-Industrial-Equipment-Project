from django.urls import path
from . import views

urlpatterns = [
    path('equipment/', views.list_equipment, name='equipment_list'),
]