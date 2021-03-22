from django.urls import path
from . import views


urlpatterns = [
    path('<page>/', views.help_center, name='help_center')
]
