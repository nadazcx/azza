# factures/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('factures/', views.FactureList.as_view(), name='facture_list'),
    path('factures/<int:pk>/', views.FactureDetail.as_view(), name='facture_detail'),
]
