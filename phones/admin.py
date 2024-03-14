from django.contrib import admin

# Register your models here.
from .models import Phone


@admin.register(Phone)
class PhoneAdmin (admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'slug']
    list_filter = ['name', 'price']
   