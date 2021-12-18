from django.contrib import admin

from achievements.admin import AchievementInline
from events.models import Event
from utils.admin import ExtendedAdmin


@admin.register(Event)
class EventAdmin(ExtendedAdmin):
    inlines = [AchievementInline]
