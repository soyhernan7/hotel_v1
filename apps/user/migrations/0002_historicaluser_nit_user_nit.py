# Generated by Django 4.2.3 on 2023-07-21 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='nit',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nit'),
        ),
        migrations.AddField(
            model_name='user',
            name='nit',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nit'),
        ),
    ]
