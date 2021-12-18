from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pgas_score = models.PositiveIntegerField(default=0, verbose_name='Баллы ПГАС')
    personal_score = models.PositiveIntegerField(default=0, verbose_name='Личные баллы')
