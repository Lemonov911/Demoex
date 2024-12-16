# Generated by Django 5.1.4 on 2024-12-14 10:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appliance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
            ],
            options={
                'verbose_name': 'вид',
                'verbose_name_plural': 'бытовая техника',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')),
                ('model', models.CharField(blank=True, max_length=100, verbose_name='модель техники')),
                ('description', models.TextField(blank=True, verbose_name='описание проблемы')),
                ('appliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repair.appliance', verbose_name='вид техники')),
                ('client', models.ForeignKey(limit_choices_to={'role': 'client'}, on_delete=django.db.models.deletion.CASCADE, related_name='my_tickets', to=settings.AUTH_USER_MODEL, verbose_name='клиент')),
                ('master', models.ForeignKey(blank=True, limit_choices_to={'role': 'master'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_tickets', to=settings.AUTH_USER_MODEL, verbose_name='мастер')),
            ],
            options={
                'verbose_name': 'тикет',
                'verbose_name_plural': 'заявки на ремонт',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата и время')),
                ('text', models.CharField(max_length=255, verbose_name='текст')),
                ('minutes', models.PositiveIntegerField(default=10, verbose_name='затрачено времени')),
                ('money', models.PositiveIntegerField(default=500, verbose_name='затрачено рублей')),
                ('author', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repair.ticket', verbose_name='заявка')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
                'ordering': ['-created'],
            },
        ),
    ]
