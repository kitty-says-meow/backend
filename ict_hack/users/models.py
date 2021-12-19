from django.contrib.auth.models import AbstractUser
from django.db import models

from events.enums import EventStatus
from trophies.models import Trophy


class User(AbstractUser):
    pgas_score = models.PositiveIntegerField(default=0, verbose_name='Баллы ПГАС')
    personal_score = models.PositiveIntegerField(default=0, verbose_name='Личные баллы')

    @property
    def achievements_confirmed(self):
        return self.achievements.filter(event__status=EventStatus.REPORT_ACCEPTED)

    @property
    def trophies(self):
        return Trophy.objects.all()
