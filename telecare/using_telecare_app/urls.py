from django.urls import path
from . import views


urlpatterns = [
    path('<page>/', views.using_telecare, name='using_telecare')
]