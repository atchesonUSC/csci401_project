from django.urls import path
from . import views


urlpatterns = [
    path('<page>/', views.internet, name='internet_check')
]
