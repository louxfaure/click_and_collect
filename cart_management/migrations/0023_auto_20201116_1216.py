# Generated by Django 3.1.3 on 2020-11-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_management', '0022_auto_20201109_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='is_peb',
            field=models.BooleanField(default=False, verbose_name='Demande de PEB ?'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='peb_descr',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='Descriptif PEB :'),
        ),
    ]
