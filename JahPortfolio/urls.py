"""
URL configuration for JahPortfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from jah_port import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.view_home, name='home'),
    path('AscendedKing', views.view_ticketmaster, name='Ascend'),
    path('Gor-3300k', views.view_cpu, name='CPU'),
    path('Jah_Simple_math_pro', views.view_simple_math_pro, name='SimpleMath'),
    path('ticketmaster', views.view_ticketmaster, name='ticketmaster'),
    path('Contact', views.contact, name='contact'),
]
