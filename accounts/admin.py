from django.contrib import admin
from .models import Refunds
# Register your models here.
class RefundsAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'car_title',)
    search_fields = ('id', 'first_name',)

    
admin.site.register(Refunds, RefundsAdmin)
