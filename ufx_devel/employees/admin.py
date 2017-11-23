from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('sim_card_number', 'first_name', 'last_name', 'is_active')
    search_fields = ('sim_card_number', 'first_name', 'last_name')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    list_per_page = 50

admin.site.register(Employee, EmployeeAdmin)
