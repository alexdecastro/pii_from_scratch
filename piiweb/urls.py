from django.urls import path
from . import views

urlpatterns = [
    # map 'piiweb/test_page/' -> ./views.py > test_page()
    path('test_page/', views.test_page, name='piiweb_test_page'),
    # map 'piiweb/test_template/' -> ./views.py > test_template()
    path('test_template/', views.test_template, name='piiweb_test_template'),
]
