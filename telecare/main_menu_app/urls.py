from django.urls import path
from . import views


urlpatterns = [
    path('install/', views.install, name='install'),
    path('internet/', views.internet, name='internet'),
    path('help_center/', views.help_center, name='help_center'),
    path('cam_mic/', views.cam_mic, name='cam_mic'),
    path('about_telehelp/', views.about_telehelp, name='about_telehelp'),
]
