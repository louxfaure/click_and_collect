# Generated by Django 3.0.6 on 2020-06-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_management', '0008_items_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='title',
            field=models.CharField(default=22, max_length=500, verbose_name="Titre de l'exemplaire"),
            preserve_default=False,
        ),
    ]
