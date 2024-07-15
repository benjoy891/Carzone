from django.contrib import admin
from .models import Contact, Favorites, Payments

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'car_title', 'city', 'created_date')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'car_title')
    list_per_page = 25

class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_title', 'created_date')  
    list_display_links = ('id','car_title',)  
    search_fields = ('car_title',)  
    list_per_page = 25

class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('id','firstname', 'lastname', 'car_title')
    search_fields = ('id', 'firstname',)

    
admin.site.register(Payments, PaymentsAdmin)
admin.site.register(Favorites, FavoritesAdmin)
admin.site.register(Contact, ContactAdmin)
