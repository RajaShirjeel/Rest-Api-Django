from django.contrib import admin
from . import models

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position')

admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Employee, EmployeeAdmin)