from django.shortcuts import render

# Create your views here.
from django.db import connection


def equipment_list(request):
    with connection.cursor() as cursor:
        # كتابة الـ SQL يدوياً زي ما مطلوب في البروجكت
        cursor.execute("SELECT * FROM Equipment")
        rows = cursor.fetchall()
    
    return render(request, 'equipment_list.html', {'equipment': rows})