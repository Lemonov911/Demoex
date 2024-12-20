# Generated by Django 5.1.4 on 2024-12-20 20:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0002_rename_deliveryrequest_supplies_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(limit_choices_to={'role': 'client'}, on_delete=django.db.models.deletion.CASCADE, related_name='my_applications', to=settings.AUTH_USER_MODEL, verbose_name='клиент')),
                ('master', models.ForeignKey(blank=True, limit_choices_to={'role': 'master'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_apps', to=settings.AUTH_USER_MODEL, verbose_name='мастер')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'заявки на поставку',
            },
        ),
    ]