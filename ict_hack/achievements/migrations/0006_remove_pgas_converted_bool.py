# Generated by Django 3.2.10 on 2021-12-19 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0005_add_pgas_converted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievement',
            name='pgas_converted',
        ),
        migrations.RemoveField(
            model_name='historicalachievement',
            name='pgas_converted',
        ),
    ]