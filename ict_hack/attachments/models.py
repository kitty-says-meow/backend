from django.db import models

from utils.models import ExtendedModel


class Image(ExtendedModel):
    file = models.ImageField(verbose_name='Файл')
