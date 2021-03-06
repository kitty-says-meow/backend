from uuid import uuid4

from django.db import models
from django.db.models import F
from django.utils import timezone

from attachments.models import Image
from departments.models import Department
from events.enums import EventCategory, EventStatus
from users.models import User
from utils.models import ExtendedModel


def event_report_upload(instance, filename):
    return f'events/reports/{uuid4()}/{filename}'


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
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Изображение')
    participants = models.ManyToManyField(User, blank=True, related_name='events', verbose_name='Участники')
    report = models.FileField(blank=True, null=True, upload_to=event_report_upload, verbose_name='Отчёт')
    status = models.PositiveSmallIntegerField(choices=EventStatus.choices, default=EventStatus.PENDING, verbose_name='Статус')

    def __str__(self):
        return f'[{self.pk}] {self.name}'

    def save(self, *args, **kwargs):
        if self.status == EventStatus.REPORT_ACCEPTED:
            achievements = self.achievements.filter(pgas_converted=None)
            for achievement in achievements:
                user = achievement.user
                if user:
                    user.pgas_score = F('pgas_score') + achievement.score
                    user.save()
            achievements.update(pgas_converted=timezone.now())
        super().save(*args, **kwargs)
