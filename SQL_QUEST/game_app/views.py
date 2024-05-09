from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import DataField, LakeData, Mountain_Of_Algorithms, Operator_Forest, Cipher_Hills, PetaByte_Bay, PetaByte_Bay2
from .models import Optimization_Plateau2, Optimization_Plateau, Index_Valley, Index_Valley2, Lunar_Landscape, Lunar_Landscape2
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


def home(request):
    return render(request, 'game_app/main_menu.html')


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


def level1(request):
    # Fetch data from the database
    sql_data = DataField.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level1.html', {'datafields': sql_data})


def level2(request):
    # Fetch data from the database
    sql_data = LakeData.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level2.html', {'LakeData': sql_data})


def level3(request):
    # Fetch data from the database
    sql_data = Mountain_Of_Algorithms.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level3.html', {'Mountain_Of_Algorithms': sql_data})


def level4(request):
    # Fetch data from the database
    sql_data = DataField.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level4.html', {'datafields': sql_data})


def level5(request):
    # Fetch data from the database
    sql_data = Operator_Forest.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level5.html', {'datafields': sql_data})


def level6(request):
    # Fetch data from both models separately
    cipher_hills_data = PetaByte_Bay.objects.all()
    cipher_hills2_data = PetaByte_Bay2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level6.html', {
        'cipher_hills_data': cipher_hills_data,
        'cipher_hills2_data': cipher_hills2_data
    })


def level7(request):
    # Fetch data from the database
    sql_data = Cipher_Hills.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level7.html', {'datafields': sql_data})


def level8(request):
    # Fetch data from both models separately
    Index_Valley_data = Index_Valley.objects.all()
    Index_Valley2_data = Index_Valley2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level6.html', {
        'cipher_hills_data': Index_Valley_data,
        'cipher_hills2_data': Index_Valley2_data
    })


def level9(request):
    # Fetch data from both models separately
    Optimization_Plateau_data = Optimization_Plateau.objects.all()
    Optimization_Plateau2_data = Optimization_Plateau2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level6.html', {
        'cipher_hills_data': Optimization_Plateau_data,
        'cipher_hills2_data': Optimization_Plateau2_data
    })


def level10(request):
    # Fetch data from both models separately
    Lunar_Landscape_data = Lunar_Landscape.objects.all()
    Lunar_Landscape2_data = Lunar_Landscape2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level6.html', {
        'cipher_hills_data': Lunar_Landscape_data,
        'cipher_hills2_data': Lunar_Landscape2_data
    })


def level11(request):
    # Fetch data from the database
    sql_data = DataField.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level11.html', {'datafields': sql_data})


def level12(request):
    # Fetch data from the database
    sql_data = DataField.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level12.html', {'datafields': sql_data})


def level13(request):
    # Fetch data from the database
    sql_data = DataField.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level13.html', {'datafields': sql_data})


def level14(request):
    # Fetch data from the database
    sql_data = DataField.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level14.html', {'datafields': sql_data})


def level15(request):
    # Fetch data from the database
    sql_data = DataField.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level15.html', {'datafields': sql_data})


def level16(request):
    # Fetch data from the database
    sql_data = DataField.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level16.html', {'datafields': sql_data})


def level17(request):
    # Fetch data from the database
    sql_data = DataField.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level17.html', {'datafields': sql_data})


def level18(request):
    # Fetch data from the database
    sql_data = DataField.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level18.html', {'datafields': sql_data})


def level19(request):
    # Fetch data from the database
    sql_data = DataField.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level19.html', {'datafields': sql_data})


def level20(request):
    # Fetch data from the database
    sql_data = DataField.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level20.html', {'datafields': sql_data})
