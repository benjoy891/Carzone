from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', admin_login, name="admin_login"),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin_cars/', admin_cars, name='admin_cars'),
    path('admin_teams/', admin_teams, name='admin_teams'),
    path('admin_contact/', admin_contact, name='admin_contact'),
    path('admin_refunds/', admin_refunds, name='admin_refunds'),
    path('admin_payments/', admin_payments, name='admin_payments'),
    path('update_car/<str:pk>', update_car, name='update_car'),
    path('team_updation/<str:pk>', team_updation, name='team_updation'),
    path('contact_details/<int:id>', contact_details, name='contact_details'),
    path('payment_details/<int:id>', payment_details, name='payment_details'),
    path('add_car/', add_car, name='add_car'),
    path('delete_car/<str:pk>', delete_car, name='delete_car'),
    path('add_team/', add_team, name='add_team'),
    path('delete_team/<str:pk>', delete_team, name='delete_team'),
]

