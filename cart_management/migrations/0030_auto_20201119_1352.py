# Generated by Django 3.1.3 on 2020-11-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_management', '0029_auto_20201119_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date et heure de création'),
        ),
        migrations.AlterField(
            model_name='items',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Date et heure de modification'),
        ),
    ]