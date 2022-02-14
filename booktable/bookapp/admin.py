from django.contrib import admin
from .models import Book
@admin.register(Book)
# Register your models here.
class Bookadmin(admin.ModelAdmin):
    list_display=('bookid','bookname','bookprice','bookpublisher')
    list_filter=('bookprice',)
    ordering=('bookname',)
    search_fields=('bookname',)
