from django.contrib import admin

from trophies.models import Trophy
from utils.admin import ExtendedAdmin


@admin.register(Trophy)
class TrophyAdmin(ExtendedAdmin):
    pass
