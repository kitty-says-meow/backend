from django.db import models

from departments.models import Department
from events.enums import EventCategory, EventStatus
from users.models import User
from utils.models import ExtendedModel


class Event(ExtendedModel):
    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Описание')
    category = models.PositiveSmallIntegerField(choices=EventCategory.choices, verbose_name='Направление')
    date_start = models.DateTimeField(blank=True, null=True, verbose_name='Дата и время начала')
    date_end = models.DateTimeField(blank=True, null=True, verbose_name='Дата и время конца')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name='Подразделение')
    participants = models.ManyToManyField(User, related_name='events', verbose_name='Участники')
    status = models.PositiveSmallIntegerField(choices=EventStatus.choices, default=EventStatus.PENDING, verbose_name='Статус')

    def __str__(self):
        return f'[{self.pk}] {self.name}'
