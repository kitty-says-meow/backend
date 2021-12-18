from django.db import models

from departments.models import Department
from events.enums import EventCategory
from utils.models import ExtendedModel


class Event(ExtendedModel):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.PositiveSmallIntegerField(choices=EventCategory.choices, verbose_name='Направление')
    date_start = models.DateTimeField(blank=True, null=True, verbose_name='Дата и время начала')
    date_end = models.DateTimeField(blank=True, null=True, verbose_name='Дата и время конца')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name='Подразделение')
