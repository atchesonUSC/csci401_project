from django.urls import path, include
from . import views


urlpatterns = [
    path('mainmenu/<int:page>/', views.main_menu, name='mainmenu'),
]