from django.urls import path
from . import views


urlpatterns = [
    path('<page>/', views.browser_check, name='browser_check')
]