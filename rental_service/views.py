from django.shortcuts import render, redirect
from django.shortcuts import render,redirect

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



def insert_yard(request):
    yard_id=request.POST.get('Yard_ID')
    local=request.POST.get('Location')
    cap=request.POST.get('Capacity')
    messageyard=''
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


# ======= SELECT All Yards ========

def select_Yard(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Yard")
        rows = cursor.fetchall()
    return render(request, 'rental_service/selectYard.html', {'yards': rows})


# ======= SELECT WITH JOIN (Equipment & Yard) ========

def select_equipment_yard(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT e.Equipment_ID, e.Model, e.Status, y.Location, y.Capacity
            FROM Equipment e
            JOIN Yard y ON e.Yard_ID = y.Yard_ID
        """)
        rows = cursor.fetchall()
    return render(request, 'rental_service/selectEquipmentYard.html', {'data': rows})


# ======= UPDATE ========

def update_equipment(request, old_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Equipment WHERE Equipment_ID = %s",
            [old_id]
        )
        row = cursor.fetchone()

    if request.method == 'POST':
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
                    UPDATE Equipment SET 
                    Equipment_ID=%s,
                    Model=%s,
                    Engine_power=%s,
                    Hourly_rental_rate=%s,
                    Status=%s,
                    Yard_ID=%s
                    WHERE Equipment_ID=%s
                    """,
                    [e_id, model, power, rate, status, yard_id, old_id]
                )

            
            return redirect('equipment_list')

        except IntegrityError:
            return render(
                request,
                'rental_service/updateEquipment.html',
                {'equipment': row, 'message': 'Data Invalid', 'color': 'red'}
            )

    return render(request, 'rental_service/updateEquipment.html', {'equipment': row})


def update_yard(request, old_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Yard WHERE Yard_ID = %s",
            [old_id]
        )
        row = cursor.fetchone()

    if request.method == 'POST':
        yard_id = request.POST.get('Yard_ID')
        loc = request.POST.get('Location')
        cap = request.POST.get('Capacity')

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE Yard SET 
                    Yard_ID=%s,
                    Location=%s,
                    Capacity=%s
                    WHERE Yard_ID=%s
                    """,
                    [yard_id, loc, cap, old_id]
                )

            
            return redirect('yard_list')

        except IntegrityError:
            return render(
                request,
                'rental_service/updateYard.html',
                {'yard': row, 'message': 'Data Invalid', 'color': 'red'}
            )

    return render(request, 'rental_service/updateYard.html', {'yard': row})
