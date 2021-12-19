# Generated by Django 3.2.10 on 2021-12-19 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('file', models.ImageField(upload_to='', verbose_name='Файл')),
                ('created_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='attachments_image_created', to=settings.AUTH_USER_MODEL, verbose_name='Кем создан')),
                ('updated_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.PROTECT, on_update=True, related_name='attachments_image_updated', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлён')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalImage',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Дата обновления')),
                ('file', models.TextField(max_length=100, verbose_name='Файл')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', django_currentuser.db.models.fields.CurrentUserField(blank=True, db_constraint=False, default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создан')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', django_currentuser.db.models.fields.CurrentUserField(db_constraint=False, default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.DO_NOTHING, on_update=True, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлён')),
            ],
            options={
                'verbose_name': 'История изменений',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
