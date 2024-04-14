from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import DataField
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection



def home(request):
    return render(request, 'game_app/main_menu.html')


def level1(request):
    # Fetch data from the database
    sql_data = DataField.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level1.html', {'datafields': sql_data})


def settings(request):
    # Add logic to start a new game (if needed)
    return render(request, 'game_app/level1.html')


def about_us(request):
    # Add logic to start a new game (if needed)
    return render(request, 'game_app/level1.html')


def leaders_sheet(request):
    # Add logic to start a new game (if needed)
    return render(request, 'game_app/level1.html')


@csrf_exempt
def execute_query(request):
    if request.method == 'POST':
        # Deserialize the JSON data from the request body
        json_data = json.loads(request.body.decode('utf-8'))
        print("Request Body:", request.body)

        # Extract the SQL query from the JSON data
        sql_query = json_data.get('sqlQuery')

        # Print or log the SQL query to inspect its value
        print("SQL Query:", sql_query)

        # Execute the SQL query against the database
        with connection.cursor() as cursor:
            try:
                cursor.execute(sql_query)
                columns = [col[0] for col in cursor.description]
                query_result = [dict(zip(columns, row)) for row in cursor.fetchall()]
                return JsonResponse(query_result, safe=False)
            except Exception as e:
                # Handle exceptions gracefully
                print("Error executing SQL query:", e)
                return JsonResponse({'error': str(e)}, status=500)
    else:
        # Handle invalid requests
        return JsonResponse({'error': 'Invalid request method'}, status=400)
