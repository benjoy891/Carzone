from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('favorites', views.favorites, name='favorites'),
    path('remove_favorite/<int:car_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('bookings', views.payments, name='bookings'),
    path('remove_booking/<int:car_id>', views.remove_from_bookings, name='remove_from_bookings'),
]
