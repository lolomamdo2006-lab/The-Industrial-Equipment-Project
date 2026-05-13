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

#######################inquiry#########################


def dashboard(request):

    with connection.cursor() as cursor:

        # 1) Most rented equipment model
        cursor.execute("""
            SELECT TOP 1
                E.MODEL,
                COUNT(R.AGREEMENT_ID) AS RENTAL_COUNT
            FROM EQUIPMENT E
            JOIN RENTAL_AGREEMENT R
                ON E.EQUIPMENT_ID = R.EQUIPMENT_ID
            GROUP BY E.MODEL
            ORDER BY RENTAL_COUNT DESC
        """)

        most_rented = cursor.fetchone()

        # 2) Top technician last month
        cursor.execute("""
            SELECT TOP 1 WITH TIES
                T.TECHNICIAN_ID,
                T.NAME,
                COUNT(S.INSPECTION_ID) AS Inspection_Count
            FROM SAFETY_RELEASE_INSPECTION S
            JOIN TECHNICIAN T
                ON S.TECHNICIAN_ID = T.TECHNICIAN_ID
            WHERE
                S.INSPECTION_DATE >= DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()) - 1, 1)
                AND S.INSPECTION_DATE < DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1)
            GROUP BY
                T.TECHNICIAN_ID, T.NAME
            ORDER BY
                Inspection_Count DESC
        """)

        technicians = cursor.fetchall()

        # 3) Contractors with no rental agreements last month
        cursor.execute("""
            SELECT C.NAME
            FROM CONTRACTOR C
            WHERE C.CONTRACTOR_ID NOT IN (
                SELECT R.CONTRACTOR_ID
                FROM RENTAL_AGREEMENT R
                WHERE MONTH(R.START_DATE) = MONTH(GETDATE()) - 1
                AND YEAR(R.START_DATE) = YEAR(GETDATE())
            )
        """)

        inactive_contractors = cursor.fetchall()

        # 4) Available machines at each yard last month
        cursor.execute("""
            SELECT 
                YARD.LOCATION AS Yard_Name,
                EQUIPMENT.MODEL,
                EQUIPMENT.EQUIPMENT_ID
            FROM EQUIPMENT
            JOIN YARD
                ON EQUIPMENT.YARD_ID = YARD.YARD_ID
            WHERE EQUIPMENT.EQUIPMENT_ID NOT IN (
                SELECT RENTAL_AGREEMENT.EQUIPMENT_ID
                FROM RENTAL_AGREEMENT
                WHERE
                    (
                        MONTH(RENTAL_AGREEMENT.START_DATE) =
                        MONTH(DATEADD(MONTH, -1, GETDATE()))
                        AND YEAR(RENTAL_AGREEMENT.START_DATE) =
                        YEAR(DATEADD(MONTH, -1, GETDATE()))
                    )
                    OR
                    (
                        MONTH(RENTAL_AGREEMENT.END_DATE_) =
                        MONTH(DATEADD(MONTH, -1, GETDATE()))
                        AND YEAR(RENTAL_AGREEMENT.END_DATE_) =
                        YEAR(DATEADD(MONTH, -1, GETDATE()))
                    )
            )
        """)

        available_machines = cursor.fetchall()

        # 5) Contractor rental hours last month
        cursor.execute("""
            SELECT 
                C.COMPANY,
                SUM(DATEDIFF(HOUR, R.START_DATE, R.END_DATE_)) AS Total_Rental_Hours
            FROM CONTRACTOR C
            JOIN RENTAL_AGREEMENT R
                ON C.CONTRACTOR_ID = R.CONTRACTOR_ID
            WHERE 
                R.START_DATE >= '2026-04-01'
                AND R.START_DATE <= '2026-04-30'
            GROUP BY C.COMPANY
        """)

        contractor_hours = cursor.fetchall()
        # 5) Contractor rental hours last month
        cursor.execute("""
SELECT YARD_ID
FROM YARD
WHERE YARD_ID NOT IN (
    SELECT E.YARD_ID
    FROM EQUIPMENT E
    JOIN RENTAL_AGREEMENT R
        ON E.EQUIPMENT_ID = R.EQUIPMENT_ID
    WHERE R.START_DATE >= DATEADD(MONTH, DATEDIFF(MONTH, 0, GETDATE()) - 1, 0)
      AND R.START_DATE < DATEADD(MONTH, DATEDIFF(MONTH, 0, GETDATE()), 0)
);
        """)

        yard_had_no_equipment= cursor.fetchall()

    context = {
        'most_rented': most_rented,
        'technicians': technicians,
        'inactive_contractors': inactive_contractors,
        'available_machines': available_machines,
        'contractor_hours': contractor_hours,
        "yard_had_no_equipment":yard_had_no_equipment,
    }

    return render(request, 'rental_service/dashboard.html', context)