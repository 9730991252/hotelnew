from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id','hotel_name','mobile','pin','status')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','employee_name','department','employee_mobile','pin','status')
