# Generated by Django 3.1.3 on 2020-11-16 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart_management', '0025_auto_20201116_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pickuplocation',
            name='closed_days',
        ),
        migrations.DeleteModel(
            name='ClosedDays',
        ),
    ]