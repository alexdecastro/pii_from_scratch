from django.urls import path
from . import views

urlpatterns = [
    path('test_page/', views.test_page, name='piiweb_test_page'),
    path('parts-addrs/<pguid_id>/', views.participantsAddressesView, name='participantsAddressesView'),
    path('addresses/<pguid_id>/', views.addressesView, name='addressesView'),
]
