"""pii URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# piiapi REST framework
from rest_framework.routers import DefaultRouter
from piiapi.views import (AddressesViewSet)
# Alternate way: import piiapi

router = DefaultRouter()
router.register(r'addresses', AddressesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # map 'http://127.0.0.1:800#/piiweb/' -> 'piiweb/urls.py'
    path('piiweb/', include('piiweb.urls')),

    # map 'http://127.0.0.1:800#/api/ -> 'piiapi/urls.py'
    path('api/', include(router.urls)),
    # Alternate way: path('api/', include('piiapi.urls')),
]
