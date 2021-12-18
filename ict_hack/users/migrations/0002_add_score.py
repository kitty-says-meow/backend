# Generated by Django 3.2.10 on 2021-12-18 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='personal_score',
            field=models.PositiveIntegerField(default=0, verbose_name='Личные баллы'),
        ),
        migrations.AddField(
            model_name='user',
            name='pgas_score',
            field=models.PositiveIntegerField(default=0, verbose_name='Баллы ПГАС'),
        ),
    ]
