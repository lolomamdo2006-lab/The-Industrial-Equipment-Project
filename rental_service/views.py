from django.shortcuts import render

# Create your views here.
from django.db import connection


def equipment_list(request):
    with connection.cursor() as cursor:
     
        cursor.execute("SELECT * FROM Equipment")
        rows = cursor.fetchall()
    
    return render(request, 'rental_service\equipment.html', {'equipment': rows})
def insert_equipment(request):
    if request.method == "POST":
        e_id = request.POST.get('Equipment_ID')
        model = request.POST.get('Model')
        power = request.POST.get('Engine_power')
        rate = request.POST.get('Hourly_rental_rate')
        status = request.POST.get('Status')
        yard_id = request.POST.get('Yard_ID')
        if yard_id == "" or yard_id is None:
            yard_id = None
        with connection.cursor() as cursor:
            cursor.execute("SELECT Equipment_ID FROM Equipment WHERE Equipment_ID = %s", [e_id])
            existing_id = cursor.fetchone()
            if existing_id:
                return render(request, 'rental_service/insertEquipment.html', {'message':"Id is exist"
                })
        with connection.cursor() as cursor:
          cursor.execute(
            "INSERT INTO Equipment (Equipment_ID, Model, Engine_power, Hourly_rental_rate, Status, Yard_ID)"
            "VALUES(%s, %s,%s,%s,%s,%s)",
            [e_id, model, power, rate, status, yard_id ]
           )
        connection.commit()
    return render(request, 'rental_service\insertEquipment.html')