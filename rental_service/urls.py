from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipment_list, name='equipment_list'),
    path('insertEquipment/', views.insert_equipment, name='insert_equipment'),
    path('insertYard/', views.insert_yard, name='insert_yard'),
    path('yard/', views.yard_list, name='yard_list'),
]