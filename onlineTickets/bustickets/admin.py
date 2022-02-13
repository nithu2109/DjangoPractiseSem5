from django.contrib import admin
from . models import BusDetails
from . models import Ticket

@admin.register(BusDetails)
@admin.register(Ticket)

# Register your models here.
class BusDetailsadmin(admin.ModelAdmin):
    list_display=('Bus_No','Destinations',)
    list_filter=('Destinations',)

# class Ticketadmin(admin.ModelAdmin):
#     list_display=('Bus_No','No_of_Persons','Destinations',)
#     list_filter=('Destinations',)