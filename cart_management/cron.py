from django.core.management.base import BaseCommand, CommandError
from django.db.models import Max, Count
from cart_management.models import Person,PickupLocation, Items
from datetime import datetime, time,timedelta
from django.core.mail import send_mail
from django.template import loader


def check_cart.py():
    now = datetime.today()
    # print(Items.objects.values('pickuplocation','person' ).filter(appointment__isnull=True).annotate(max_date=Max('created')))       
    for resas_ss_rdv in Items.objects.values('pickuplocation','person' ).filter(appointment__isnull=True, relance_mail=0).annotate(max_date=Max('created')):
        print(resas_ss_rdv)
        time_delta = resas_ss_rdv['max_date'] - now
        delta_in_seconds = time_delta.seconds
        print(delta_in_seconds)
        delta_in_minutes = delta_in_seconds / 60.
        print(delta_in_minutes)
        if delta_in_minutes > 60 :
            print("on va faire le job !")
        pickup_loc = PickupLocation.objects.get(id_alma=resas_ss_rdv['pickuplocation'])
        lecteur = Person.objects.get(id_alma=resas_ss_rdv['person'])
        url_to_primo = "https://babordplus.hosted.exlibrisgroup.com/primo-explore/account?vid=33PUDB_{}_VU1&section=requests&lang=fr_FR".format(pickup_loc.institution)
        html_message = loader.render_to_string("cart_management/mail_prise_rdv.html", locals())
        for resas_lecteurs in Items.objects.filter(appointment__isnull=True,pickuplocation=pickup_loc,person=lecteur):
            resas_lecteurs.relance_mail =+ 1
            resas_lecteurs.save()
            print(resas_lecteurs)

        send_mail(
            "{} : Vous devez choisir un créneau de retrait afin de valider votre réservation".format(pickup_loc.name),
            "Ce message contient en pièce jointe un message de votre bibliothèque.",
            pickup_loc.from_email,
            [lecteur.email],
            fail_silently=False,
            html_message=html_message,
        )
    #     for lect in Items.objects.values('person').filter(appointment__isnull=True, pickuplocation=bib['pickuplocation']).distinct():
    #         print(lect)
    #         resas_ss_rdv = Items.objects.filter(appointment__isnull=True, pickuplocation=bib['pickuplocation'], person=lect['person']).aggregate(Max('created'))
    #         print(resas_ss_rdv.title)
    #         self.stdout.write(self.style.SUCCESS(resas_ss_rdv))