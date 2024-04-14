from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('level_1/', views.level1, name='level1'),
    path('execute_query/', views.execute_query, name='execute_query'),
    path('leaders_sheet/', views.leaders_sheet, name='leaders_sheet'),
    path('settings/', views.settings, name='settings'),
    path('about_us/', views.about_us, name='about_us'),
]