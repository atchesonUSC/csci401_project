from django.urls import path
from . import views


urlpatterns = [
    path('', views.cam_mic_user_status, name='user_status'),
    path('new/<page>/', views.cam_mic_new, name='cam_mic_new'),
    path('returning/<page>/', views.cam_mic_returning, name='cam_mic_returning'),
]