from django.shortcuts import render, redirect

# Create your views here.
from django.db import connection

from django.db import IntegrityError

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

        try:
            with connection.cursor() as cursor:

                cursor.execute(
                    """
                    INSERT INTO Equipment
                    (Equipment_ID, Model, Engine_power,
                    Hourly_rental_rate, Status, Yard_ID)

                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    [e_id, model, power, rate, status, yard_id]
                )
                connection.commit()

            return render(
                request,
                'rental_service/insertEquipment.html',
                {'message': 'Inserted Successfully','color':'rgb(101, 192, 27)'}
            )

        except IntegrityError:

            return render(
                request,
                'rental_service/insertEquipment.html',
                {'message': 'Data Invalid','color':'rgb(192, 27, 27)'}
            )

    return render(request, 'rental_service/insertEquipment.html')

# 

# try:
#     with connection.cursor() as cursor:
#         cursor.execute("INSERT INTO Equipment ...", [e_id, ...])
#         connection.commit()
# except IntegrityError:
#     # هنا بنقفش الـ Error لو الـ ID اتكرر
#     return render(request, 'insert.html', {'message': 'الـ ID ده مستخدم قبل كدة، جرب غيره!'})

def insert_yard(request):
    yard_id=request.POST.get('Yard_ID')
    local=request.POST.get('Location')
    cap=request.POST.get('Capacity')
    try:
        with connection.cursor() as cursor:

                cursor.execute(
                    """
                    INSERT INTO Yard
                    (Yard_ID,Location, Capacity)

                    VALUES (%s, %s, %s)
                    """,
                    [ yard_id,local, cap]
                )
                connection.commit()

        return render(
                request,
                'rental_service/insertYard.html',
                {'messageyard': 'Inserted Successfully','color':'rgb(101, 192, 27)'}
            )

    except IntegrityError:
            return render(
                request,
                'rental_service/insertYard.html',
                {'messageyard': 'Data Invalid','color':'rgb(192, 27, 27)'}
            )

    return render(request, 'rental_service/insertYard.html')
def yard_list(request):
    with connection.cursor() as cursor:
     
        cursor.execute("SELECT * FROM Yard")
        rows = cursor.fetchall()
    
    return render(request, 'rental_service\yard.html', {'yard': rows})

# ===== DELETE =====

def delete_equipment(request):
    if request.method == "POST":
        equipment_id = request.POST.get('Equipment_ID')
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Equipment WHERE Equipment_ID = %s",
                    [equipment_id]
                )
                connection.commit()
            return redirect('equipment_list')
        except IntegrityError:
            return redirect(f'/yard/?error=Cannot delete: This yard has equipment assigned to it')

    return redirect('equipment_list')


def delete_yard(request):
    if request.method == "POST":
        yard_id = request.POST.get('Yard_ID')
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Yard WHERE Yard_ID = %s",
                    [yard_id]
                )
                connection.commit()
        except IntegrityError:
            return redirect(f'/yard/?error=Cannot delete: This yard has equipment assigned to it')

    return redirect('yard_list')

