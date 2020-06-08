# Generated by Django 3.0.6 on 2020-05-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PickupLocation',
            fields=[
                ('id_alma', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Identifiant Alma')),
                ('name', models.CharField(max_length=200, verbose_name='Nom de la bibliotheque')),
                ('institution', models.CharField(choices=[('BXSA', 'Bordeaux Sciences Agro'), ('INP', 'INP Bordeaux'), ('IEP', 'Sciences Po Bordeaux'), ('UBM', 'Université Bordeaux Montaigne'), ('UB', 'Université de Bordeaux')], default='UB', max_length=5, verbose_name="Code l'institution ")),
                ('plot_number', models.IntegerField(default=1, verbose_name='Nombre de plages par heure')),
                ('handling_time', models.IntegerField(default=2, verbose_name='Délai en jour pour la préparation de la commande')),
                ('handling_time_external_library', models.IntegerField(default=7, verbose_name="Délai en jours pour la préparation de la commande quand le document vient d'une autre bibliothèque")),
                ('open_hour', models.IntegerField(default=9, verbose_name="Heure d'ouverture du service de retrait")),
                ('close_hour', models.IntegerField(default=17, verbose_name="Heure d'ouverture du service de retrait")),
                ('days_for_booking', models.IntegerField(default=10, verbose_name='Nombre de jours à proposer pour la prise de rdv')),
                ('email', models.EmailField(default='alexandre.faure@u-bordeaux.fr', max_length=254, verbose_name='Adresse vers laquelle envoyer la liste des documents résercés')),
                ('url', models.URLField(blank=True, default='', verbose_name="Lien vers les informations d'accès à la bibliothèque")),
                ('message', models.CharField(blank=True, default='', max_length=500, verbose_name='Message')),
                ('lat', models.CharField(blank=True, default='', max_length=50, verbose_name='Latitude')),
                ('longitude', models.CharField(blank=True, default='', max_length=50, verbose_name='Longitude')),
            ],
        ),
    ]
