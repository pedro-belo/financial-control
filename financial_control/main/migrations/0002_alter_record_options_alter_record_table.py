# Generated by Django 4.1.3 on 2022-11-29 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': 'Record', 'verbose_name_plural': 'Records'},
        ),
        migrations.AlterModelTable(
            name='record',
            table='main_record',
        ),
    ]
