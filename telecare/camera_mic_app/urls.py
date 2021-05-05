from django.urls import path
from . import views


urlpatterns = [
    path('<page>/', views.cam_mic, name='cam_mic'),

    # path('', views.cam_mic_user_status, name='cam_mic'),
    # path('system/', views.cam_mic_user_status1, name='cam_mic_system'),
    # path('ios/', views.cam_mic_user_status2, name='cam_mic_ios_help'),
    # path('android/', views.cam_mic_user_status3, name='cam_mic_android_help'),
    # path('new/<page>/', views.cam_mic_new, name='cam_mic_new'),
    # path('returning/<page>/', views.cam_mic_returning, name='cam_mic_returning'),
]
