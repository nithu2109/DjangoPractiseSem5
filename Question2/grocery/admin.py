from django.contrib import admin
from .models import Grocery
@admin.register(Grocery)
# Register your models here.
class GroceryAdmin(admin.ModelAdmin):
   list_display=('name','type','quantity','rate_per_unit','amount',)
   list_filter=('name',)