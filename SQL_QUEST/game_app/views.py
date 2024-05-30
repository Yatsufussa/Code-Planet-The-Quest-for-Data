from django.shortcuts import render, redirect
from django.db.models import Sum, Count, DurationField, IntegerField
from django.db.models.functions import Coalesce
from .models import DataField, LakeData, Mountain_Of_Algorithms, Operator_Forest, Cipher_Hills, PetaByte_Bay, Pass, \
    PetaByte_Bay2, Player, Level, ExperiencePoints, Log_Desrt, PlanetDungeons, PlanetDungeons2, ArchivesCity, \
    ArchivesCity2, FinalShowdown, FinalShowdown2, RetryAttempt
from .models import Optimization_Plateau2, Optimization_Plateau, Index_Valley, Index_Valley2, Lunar_Landscape, \
    Lunar_Landscape2, QueryFactory, QueryFactory2, APIFields, APIFields2, HiddenTreasure, Answers, Hints
from .models import SecurityCastle, SecurityCastle2, ProcessingClouds, ProcessingClouds2, DatabaseDepths, \
    DatabaseDepths2, CodeCodeksRidge, CodeCodeksRidge2, DataManagementCenter, DataManagementCenter2
import json
from django.db.models import F
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from .forms import PlayerRegistrationForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Player, Level, Pass, ExperiencePoints, Performance
import json
from datetime import timedelta


def register_player(request):
    if request.method == 'POST':
        form = PlayerRegistrationForm(request.POST)
        if form.is_valid():
            player = form.save()
            request.session['player_id'] = player.id
            return redirect('main_menu')
    else:
        form = PlayerRegistrationForm()
    return render(request, 'game_app/registration.html', {'form': form})


def leaderboard(request):
    # Annotate players with the total completion time and count of distinct levels passed
    leaderboard_data = (
        Pass.objects.values('player__nickname')
        .annotate(total_time=Coalesce(Sum('time'), 0, output_field=DurationField()))  # Coalesce to handle NULL values
        .annotate(rounds_passed=Count('level', distinct=True, output_field=IntegerField()))
        .order_by('-rounds_passed', 'total_time')  # Order by rounds_passed descending, total_time ascending
    )
    return render(request, 'game_app/leaderboard.html', {'leaderboard_data': leaderboard_data})


def get_player_id(request):
    if request.method == 'GET':
        player_id = request.session.get('player_id')
        if player_id:
            return JsonResponse({'player_id': player_id})
        else:
            return JsonResponse({'error': 'Player ID not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_hint(request):
    level_id = request.GET.get('level_id')
    try:
        hint = Hints.objects.get(level_id=level_id).hint
        return JsonResponse({'hint': hint})
    except Hints.DoesNotExist:
        return JsonResponse({'hint': 'No hint available for this level.'}, status=404)


@csrf_exempt
def record_level_completion(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            player_id = json_data.get('player_id')
            level_id = json_data.get('level_id')
            elapsed_time = json_data.get('elapsed_time')
            retry_count = json_data.get('retry_count')

            if not player_id or not level_id or not elapsed_time or retry_count is None:
                return JsonResponse({'error': 'Missing data'}, status=400)

            print(
                f"Received data: player_id={player_id}, level_id={level_id}, elapsed_time={elapsed_time}, retry_count={retry_count}")

            elapsed_time = timedelta(seconds=elapsed_time)
            level = Level.objects.get(id=level_id)
            player = Player.objects.get(id=player_id)
            performance = Performance.objects.get(level=level)

            if elapsed_time <= performance.top_time:
                stars = 3
            elif elapsed_time <= performance.medium_time:
                stars = 2
            else:
                stars = 1

            Pass.objects.create(
                player=player,
                level=level,
                time=elapsed_time,
                stars=stars,
                retry_count=retry_count
            )

            base_points = 100
            multiplier = 2 if stars == 3 else 1.5 if stars == 2 else 1
            total_points = int(base_points * multiplier)

            ExperiencePoints.objects.create(
                player=player,
                level=level,
                points=total_points
            )

            total_experience_points = ExperiencePoints.objects.filter(player=player).aggregate(total=Sum('points'))[
                'total']
            new_level = total_experience_points // 1000
            print(f"Current player level: {player.p_level}, New level: {new_level}")

            if player.p_level != new_level:
                player.p_level = new_level
                player.save()
                print(f"Player level updated to {new_level}")
            else:
                print("Player level remains unchanged")

            return JsonResponse({'success': True})
        except Exception as e:
            print(f"Exception: {e}")
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


def home(request):
    return render(request, 'game_app/main_menu.html')


def settings(request):
    # Add logic to start a new game (if needed)
    return render(request, 'game_app/level1.html')


def about_us(request):
    # Add logic to start a new game (if needed)
    return render(request, 'game_app/level1.html')


@csrf_exempt
def increment_player_level(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            player_id = data.get('player_id')

            if not player_id:
                return JsonResponse({'error': 'Player ID is required'}, status=400)

            player = Player.objects.get(id=player_id)

            # Ensure p_level is not None
            if player.p_level is None:
                player.p_level = 0

            player.p_level += 1
            player.save()

            return JsonResponse({'success': True})
        except Player.DoesNotExist:
            return JsonResponse({'error': 'Player not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


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
    sql_data = Log_Desrt.objects.all()  # Query your database to retrieve data
    # Pass the data to the template
    return render(request, 'game_app/level4.html', {'Log_Desrt': sql_data})


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
    return render(request, 'game_app/level8.html', {
        'cipher_hills_data': Index_Valley_data,
        'cipher_hills2_data': Index_Valley2_data
    })


def level9(request):
    # Fetch data from both models separately
    Optimization_Plateau_data = Optimization_Plateau.objects.all()
    Optimization_Plateau2_data = Optimization_Plateau2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level9.html', {
        'cipher_hills_data': Optimization_Plateau_data,
        'cipher_hills2_data': Optimization_Plateau2_data
    })


def level10(request):
    # Fetch data from both models separately
    Lunar_Landscape_data = Lunar_Landscape.objects.all()
    Lunar_Landscape2_data = Lunar_Landscape2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level10.html', {
        'cipher_hills_data': Lunar_Landscape_data,
        'cipher_hills2_data': Lunar_Landscape2_data
    })


def level11(request):
    # Fetch data from both models separately
    PlanetDungeons_data = PlanetDungeons.objects.all()
    PlanetDungeons2_data = PlanetDungeons2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level11.html', {
        'cipher_hills_data': PlanetDungeons_data,
        'cipher_hills2_data': PlanetDungeons2_data
    })


def level12(request):
    # Fetch data from both models separately
    ArchivesCity_data = ArchivesCity.objects.all()
    ArchivesCityw_data = ArchivesCity2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level12.html', {
        'cipher_hills_data': ArchivesCity_data,
        'cipher_hills2_data': ArchivesCityw_data
    })


def level13(request):
    # Fetch data from both models separately
    QueryFactory_data = QueryFactory.objects.all()
    QueryFactory2_data = QueryFactory2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level13.html', {
        'cipher_hills_data': QueryFactory_data,
        'cipher_hills2_data': QueryFactory2_data
    })


def level14(request):
    # Fetch data from both models separately
    APIFields_data = APIFields.objects.all()
    APIFields2_data = APIFields2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level14.html', {
        'cipher_hills_data': APIFields_data,
        'cipher_hills2_data': APIFields2_data
    })


def level15(request):
    # Fetch data from both models separately
    SecurityCastle_data = SecurityCastle.objects.all()
    SecurityCastle2_data = SecurityCastle2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level15.html', {
        'cipher_hills_data': SecurityCastle_data,
        'cipher_hills2_data': SecurityCastle2_data
    })


def level16(request):
    # Fetch data from both models separately
    ProcessingClouds_data = ProcessingClouds.objects.all()
    ProcessingClouds2_data = ProcessingClouds2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level16.html', {
        'cipher_hills_data': ProcessingClouds_data,
        'cipher_hills2_data': ProcessingClouds2_data
    })


def level17(request):
    # Fetch data from both models separately
    DatabaseDepths_data = DatabaseDepths.objects.all()
    DatabaseDepths2_data = DatabaseDepths2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level17.html', {
        'cipher_hills_data': DatabaseDepths_data,
        'cipher_hills2_data': DatabaseDepths2_data
    })


def level18(request):
    # Fetch data from both models separately
    CodeCodeksRidge_data = CodeCodeksRidge.objects.all()
    CodeCodeksRidge2_data = CodeCodeksRidge2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level18.html', {
        'cipher_hills_data': CodeCodeksRidge_data,
        'cipher_hills2_data': CodeCodeksRidge2_data
    })


def level19(request):
    # Fetch data from both models separately
    DataManagementCenter_data = DataManagementCenter.objects.all()
    DataManagementCenter2_data = DataManagementCenter2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level19.html', {
        'cipher_hills_data': DataManagementCenter_data,
        'cipher_hills2_data': DataManagementCenter2_data
    })


def level20(request):
    # Fetch data from both models separately
    FinalShowdown_data = FinalShowdown.objects.all()
    FinalShowdown2_data = FinalShowdown2.objects.all()

    # Pass the data from each model separately to the template
    return render(request, 'game_app/level20.html', {
        'cipher_hills_data': FinalShowdown_data,
        'cipher_hills2_data': FinalShowdown2_data
    })
