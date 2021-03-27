from django.urls import path
from . import views


urlpatterns = [
    path('<page>/', views.about, name='about_telehelp')
]

