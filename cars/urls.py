from django.urls import path
from . import views


urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_detail, name='car_detail'),
    path('search', views.search, name='search'),
    path('payment_success', views.payment_success, name='payment_success'),
    path('razor', views.razor, name='razor'),
]
