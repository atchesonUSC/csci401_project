"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('welcome_app.urls')),
    path('readiness_check/', include('readiness_check_app.urls')),
    path('install/', include('install_app.urls')),
    path('cam_mic/', include('camera_mic_app.urls')),
    path('about_telehelp/', include('about_telehelp_app.urls')),
    path('browser/', include('browser_check_app.urls')),
    path('waiting_room/', include('waiting_room_app.urls')),
    path('using_telecare/', include('using_telecare_app.urls')),
]
