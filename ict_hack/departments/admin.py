from django.contrib import admin

from departments.models import Department
from utils.admin import ExtendedAdmin


@admin.register(Department)
class DepartmentAdmin(ExtendedAdmin):
    pass
