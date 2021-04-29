from django.urls import path
from . import views

urlpatterns = [
    path('test_page/', views.test_page, name='piiweb_test_page'),
    path('addresses/<pguid_id>/', views.addressesView, name='addressesView'),
    path('addresses/address-select/<pguid_id>/', views.addressSelectView, name='address-select'),
    path('addresses/create_part_addr/<pguid_id>/<addr_id>/', views.create_part_addr, name='create_part_addr'),
    path('addresses/delete_part_addr/<pguid_id>/<addr_id>/', views.delete_part_addr, name='delete_part_addr'),
]
