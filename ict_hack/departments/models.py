import os
from uuid import uuid4

from django.db import models

from users.models import User
from utils.models import ExtendedModel


def department_logo_upload(instance, filename):
    file_name, file_extension = os.path.splitext(filename)

    return f'departments/logos/{uuid4()}{file_extension}'


class Department(ExtendedModel):
    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=2000, verbose_name='Описание')
    link = models.URLField(verbose_name='Ссылка')
    logo = models.ImageField(upload_to=department_logo_upload, verbose_name='Логотип')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='departments', verbose_name='Руководитель')
