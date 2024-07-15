from django.urls import path
from . import views


urlpatterns = [
    path('inquiry', views.inquiry, name='inquiry'),
    path('favorite', views.favorite, name='favorite'),
    path('payment',views.payment, name='payment'),
]
