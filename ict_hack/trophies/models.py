from django.db import models

from events.enums import EventCategory
from utils.models import ExtendedModel


class Trophies(models.IntegerChoices):
    EDUCATION_5 = 1, 'Учеба - 5'
    EDUCATION_10 = 2, 'Учеба - 10'
    SCIENCE_5 = 3, 'Учеба - 5'
    SCIENCE_10 = 4, 'Учеба - 10'
    SOCIAL_5 = 5, 'Учеба - 5'
    SOCIAL_10 = 6, 'Учеба - 10'
    CULTURE_5 = 7, 'Учеба - 5'
    CULTURE_10 = 8, 'Учеба - 10'
    SPORT_5 = 9, 'Учеба - 5'
    SPORT_10 = 10, 'Учеба - 10'
    PGAS_TOP3 = 11, 'Топ-3 в рейтинге'


class Trophy(ExtendedModel):
    class Meta:
        verbose_name = 'Трофей'
        verbose_name_plural = 'Трофеи'

    code = models.PositiveSmallIntegerField(choices=Trophies.choices, verbose_name='Код')
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=200, verbose_name='Описание')
    category = models.PositiveSmallIntegerField(choices=EventCategory.choices, blank=True, null=True, verbose_name='Категория')

    def __str__(self):
        return f'[Код {self.code}] {self.name}'