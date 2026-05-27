from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_shipment, name='search_shipment'),
]
