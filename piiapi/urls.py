from django.urls import include, path
from .import views


urlpatterns = [
    # map 'piiapi/addresses/' -> ./views.py > AddressesViewSet()
    path('addresses/', views.AddressesViewSet),
]
