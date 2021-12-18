from django.contrib import admin

from achievements.models import Achievement
from utils.admin import ExtendedAdmin


@admin.register(Achievement)
class AchievementAdmin(ExtendedAdmin):
    pass


class AchievementInline(admin.TabularInline):
    model = Achievement
    extra = 0
