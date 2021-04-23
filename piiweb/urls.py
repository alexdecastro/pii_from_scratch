from django.urls import path
from . import views

urlpatterns = [
    path('test_page/', views.test_page, name='piiweb_test_page'),
    path('addresses/<pguid_id>/', views.addressesView, name='addressesView'),
    path('addresses/address-select/<pguid_id>/', views.addressSelectView, name='addressSelect'),
]
