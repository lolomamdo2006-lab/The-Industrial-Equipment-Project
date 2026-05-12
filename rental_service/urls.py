from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipment_list, name='equipment_list'),
    path('insertEquipment/', views.insert_equipment, name='insert_equipment'),
    path('insertYard/', views.insert_yard, name='insert_yard'),
    path('yard/', views.yard_list, name='yard_list'),
    path('updateEquipment/<int:old_id>', views.update_equipment, name='update_equipment'),
    path('updateYard/<int:old_id>', views.update_yard, name='update_yard'),

    path('deleteEquipment/', views.delete_equipment, name='delete_equipment'),
    path('deleteYard/', views.delete_yard, name='delete_yard'),

    # path('selectYard/', views.select_Yard, name='select_Yard'),
]