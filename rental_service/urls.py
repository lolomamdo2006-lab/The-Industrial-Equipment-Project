from django.urls import path
from . import views

urlpatterns = [
    path('equipment/', views.equipment_list, name='equipment_list'),
    path('insertEquipment/', views.insert_equipment, name='insert_equipment'),
]