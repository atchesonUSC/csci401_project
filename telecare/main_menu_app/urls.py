from django.urls import path, include
from . import views


urlpatterns = [
    path('<page>/', views.main_menu, name='mainmenu'),
]
