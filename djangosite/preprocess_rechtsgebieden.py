# -*- coding: utf-8 -*-
# gurdjieff/models.py
import os,sys
import datetime
import django

#  you have to set the correct path to you settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gurdjieff.settings')
try:
    from django.core.management import execute_from_command_line
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exc

django.setup()
from app.models import Rechtsgebied

def process_rechtsgebied(rechtsgebied):
    q = Rechtsgebied.objects.filter(naam=rechtsgebied)
    if q:
        q.delete()

    u = Rechtsgebied(naam=rechtsgebied)
    u.save()

def process_rechtsgebieden():
   
    process_rechtsgebied('Bestuursrecht')
    process_rechtsgebied('Bestuursrecht_Ambtenarenrecht')
    process_rechtsgebied('Bestuursrecht_Belastingrecht')
    process_rechtsgebied('Bestuursrecht_Bestuursprocesrecht')
    process_rechtsgebied('Bestuursrecht_Bestuursstrafrecht')
    process_rechtsgebied('Bestuursrecht_Europees bestuursrecht')
    process_rechtsgebied('Bestuursrecht_Mededingingsrecht')
    process_rechtsgebied('Bestuursrecht_Omgevingsrecht')
    process_rechtsgebied('Bestuursrecht_Socialezekerheidsrecht')
    process_rechtsgebied('Bestuursrecht_Bestuursrecht_Vreemdelingenrecht')
    
    process_rechtsgebied('Civielrecht')
    process_rechtsgebied('Civielrecht_Aanbestedingsrecht')
    process_rechtsgebied('Civielrecht_Arbeidsrecht')
    process_rechtsgebied('Civielrecht_Burgerlijk procesrecht')
    process_rechtsgebied('Civielrecht_Europees civiel recht')
    process_rechtsgebied('Civielrecht_Goederenrecht')
    process_rechtsgebied('Civielrecht_Insolventierecht')
    process_rechtsgebied('Civielrecht_Intellectueel-eigendomsrecht')
    process_rechtsgebied('Civielrecht_Internationaal privaatrecht')
    process_rechtsgebied('Civielrecht_Mededingingsrecht')
    process_rechtsgebied('Civielrecht_Ondernemingsrecht')
    process_rechtsgebied('Civielrecht_Personen- en familierecht')
    process_rechtsgebied('Civielrecht_Verbintenissenrecht')

    process_rechtsgebied('Strafrecht')
    process_rechtsgebied('Strafrecht_Europees strafrecht')
    process_rechtsgebied('Strafrecht_Internationaal strafrecht')
    process_rechtsgebied('Strafrecht_Materieel strafrecht')
    process_rechtsgebied('Strafrecht_Penitentiair strafrecht')
    process_rechtsgebied('Strafrecht_Strafprocesrecht')

    process_rechtsgebied('Internationaal publiekrecht')
    process_rechtsgebied('Internationaal publiekrecht_Mensenrechten')
    process_rechtsgebied('Internationaal publiekrecht_Volkenrecht')

if __name__ == "__main__":
    process_rechtsgebieden()
