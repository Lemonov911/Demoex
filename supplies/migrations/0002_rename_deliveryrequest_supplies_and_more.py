# Generated by Django 5.1.4 on 2024-12-20 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DeliveryRequest',
            new_name='Supplies',
        ),
        migrations.AlterModelOptions(
            name='supplies',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]