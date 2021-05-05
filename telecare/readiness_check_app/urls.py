from django.urls import path
from . import views


urlpatterns = [
    path('<page>/', views.readiness, name='readiness_check')
]
