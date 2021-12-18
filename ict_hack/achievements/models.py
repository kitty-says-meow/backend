from django.core.validators import MinValueValidator
from django.db import models

from events.models import Event
from users.models import User
from utils.models import ExtendedModel


class Achievement(ExtendedModel):
    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

    event = models.ForeignKey(Event, on_delete=models.PROTECT, null=True, related_name='achievements', verbose_name='Мероприятие')
    name = models.CharField(max_length=100, verbose_name='Название')
    score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], verbose_name='Баллы')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='achievements', verbose_name='Пользователь')
