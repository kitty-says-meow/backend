from django.db import models

from events.enums import EventCategory
from utils.models import ExtendedModel


class Trophies(models.IntegerChoices):
    EDUCATION_5 = 1, 'Учеба - 5'
    EDUCATION_10 = 2, 'Учеба - 10'
    SCIENCE_5 = 3, 'Наука - 5'
    SCIENCE_10 = 4, 'Наука - 10'
    SOCIAL_5 = 5, 'Активность - 5'
    SOCIAL_10 = 6, 'Активность - 10'
    CULTURE_5 = 7, 'Культура - 5'
    CULTURE_10 = 8, 'Культура - 10'
    SPORT_5 = 9, 'Спорт - 5'
    SPORT_10 = 10, 'Спорт - 10'
    PGAS_TOP3 = 11, 'Топ-3 в рейтинге'


def trophy_icon_upload(instance, filename):
    return f'trophies/icons/{instance.code}.svg'


class Trophy(ExtendedModel):
    class Meta:
        verbose_name = 'Трофей'
        verbose_name_plural = 'Трофеи'
        ordering = ('code',)

    code = models.PositiveSmallIntegerField(choices=Trophies.choices, verbose_name='Код')
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=200, verbose_name='Описание')
    category = models.PositiveSmallIntegerField(choices=EventCategory.choices, blank=True, null=True, verbose_name='Категория')
    icon = models.FileField(upload_to=trophy_icon_upload, verbose_name='Иконка')

    def __str__(self):
        return f'[Код {self.code}] {self.name}'
