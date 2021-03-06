from django.urls import path
from . import views

urlpatterns = [
    path('test_page/', views.test_page, name='piiweb_test_page'),
    path('teacher-survey/<slug:teachersurveyid>/', views.teacherSurveyView.as_view(), name='teacherSurveyView'),
    path('participants/participant-view/<slug:pguid>/', views.participantView.as_view(), name='participantView'),
    path('participants/participant-new/', views.participantNewView.as_view(), name='participantNewView'),

    path('addresses/address-view-old/<slug:addr_id>/', views.addressView1.as_view(), name='addressView1'),
    path('addresses/address-new-old/', views.addressNewView1.as_view(), name='addressNewView1'),
    path('addresses/address-edit/<slug:addr_id>/', views.addressEditView, name='addressEditView'),
    path('addresses/address-new/', views.addressNewView, name='addressNewView'),

    path('addresses_old/', views.addressesViewOld, name='addressesViewOld'),
    path('addresses/', views.addressesView, name='addressesView'),

    path('addresses/address-select/<pguid_id>/', views.addressSelectView, name='addressSelectView'),
    path('addresses/create_part_addr/<pguid_id>/<addr_id>/', views.create_part_addr, name='create_part_addr'),
    path('addresses/delete_part_addr/<pguid_id>/<addr_id>/', views.delete_part_addr, name='delete_part_addr'),

    path('addresses/address-new-pguid/<pguid_id>/', views.addressNewViewForPguid, name='addressNew'),
]
