from . import views
from django.urls import path

urlpatterns = [
    path('', views.register_player, name='register_player'),  # URL pattern for player registration
    path('main_menu/', views.home, name='main_menu'),
    path('get_player_id/', views.get_player_id, name='get_player_id'),
    path('register_player/', views.register_player, name='register_player'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('record_level_completion/', views.record_level_completion, name='record_level_completion'),
    path('execute_query/', views.execute_query, name='execute_query'),
    path('settings/', views.settings, name='settings'),
    path('about_us/', views.about_us, name='about_us'),
    path('level1/', views.level1, name='level1'),
    path('level2/', views.level2, name='level2'),
    path('level3/', views.level3, name='level3'),
    path('level4/', views.level4, name='level4'),
    path('level5/', views.level5, name='level5'),
    path('level6/', views.level6, name='level6'),
    path('level7/', views.level7, name='level7'),
    path('level8/', views.level8, name='level8'),
    path('level9/', views.level9, name='level9'),
    path('level10/', views.level10, name='level10'),
    path('level11/', views.level11, name='level11'),
    path('level12/', views.level12, name='level12'),
    path('level13/', views.level13, name='level13'),
    path('level14/', views.level14, name='level14'),
    path('level15/', views.level15, name='level15'),
    path('level16/', views.level16, name='level16'),
    path('level17/', views.level17, name='level17'),
    path('level18/', views.level18, name='level18'),
    path('level19/', views.level19, name='level19'),
    path('level20/', views.level20, name='level20'),
]