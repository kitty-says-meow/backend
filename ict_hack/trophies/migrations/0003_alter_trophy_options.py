# Generated by Django 3.2.10 on 2021-12-19 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trophies', '0002_alter_trophy_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trophy',
            options={'ordering': ('code',), 'verbose_name': 'Трофей', 'verbose_name_plural': 'Трофеи'},
        ),
    ]
