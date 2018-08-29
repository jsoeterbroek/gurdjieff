# -*- coding: utf-8 -*-
# gurdjieff/models.py
import datetime
from gurdjieff import app, db, bcrypt
from gurdjieff.models import Rechtsgebied

def process_rechtsgebied(rechtsgebied,hoofdrechtsgebied):
    d = db.session.query(Rechtsgebied).filter_by(naam=rechtsgebied).first() or None
    if d:
        db.session.delete(d)
    u = Rechtsgebied(rechtsgebied)
    #h = db.session.query(Hoofdrechtsgebied).filter_by(naam=hoofdrechtsgebied).first()
    db.session.add(u)
    #h.subs.append(u)
    db.session.commit()

def process_rechtsgebieden():
   
    process_rechtsgebied('Bestuursrecht', 'Bestuursrecht')
    process_rechtsgebied('Bestuursrecht_Ambtenarenrecht', 'Bestuursrecht')
    process_rechtsgebied('Bestuursrecht_Belastingrecht', 'Bestuursrecht')
    process_rechtsgebied('Bestuursrecht_Bestuursprocesrecht', 'Bestuursrecht')
    process_rechtsgebied('Bestuursrecht_Bestuursstrafrecht', 'Bestuursrecht')
    process_rechtsgebied('Bestuursrecht_Europees bestuursrecht', 'Bestuursrecht')
    process_rechtsgebied('Bestuursrecht_Mededingingsrecht', 'Bestuursrecht')
    process_rechtsgebied('Bestuursrecht_Omgevingsrecht', 'Bestuursrecht')
    process_rechtsgebied('Bestuursrecht_Socialezekerheidsrecht', 'Bestuursrecht')
    process_rechtsgebied('Bestuursrecht_Bestuursrecht_Vreemdelingenrecht', 'Bestuursrecht')
    
    process_rechtsgebied('Civielrecht', 'Civielrecht')
    process_rechtsgebied('Civielrecht_Aanbestedingsrecht', 'Civielrecht')
    process_rechtsgebied('Civielrecht_Arbeidsrecht', 'Civielrecht')
    process_rechtsgebied('Civielrecht_Burgerlijk procesrecht', 'Civielrecht')
    process_rechtsgebied('Civielrecht_Europees civiel recht', 'Civielrecht')
    process_rechtsgebied('Civielrecht_Goederenrecht', 'Civielrecht')
    process_rechtsgebied('Civielrecht_Insolventierecht', 'Civielrecht')
    process_rechtsgebied('Civielrecht_Intellectueel-eigendomsrecht', 'Civielrecht')
    process_rechtsgebied('Civielrecht_Internationaal privaatrecht', 'Civielrecht')
    process_rechtsgebied('Civielrecht_Mededingingsrecht', 'Civielrecht')
    process_rechtsgebied('Civielrecht_Ondernemingsrecht', 'Civielrecht')
    process_rechtsgebied('Civielrecht_Personen- en familierecht', 'Civielrecht')
    process_rechtsgebied('Civielrecht_Verbintenissenrecht', 'Civielrecht')

    process_rechtsgebied('Strafrecht', 'Strafrecht')
    process_rechtsgebied('Strafrecht_Europees strafrecht', 'Strafrecht')
    process_rechtsgebied('Strafrecht_Internationaal strafrecht', 'Strafrecht')
    process_rechtsgebied('Strafrecht_Materieel strafrecht', 'Strafrecht')
    process_rechtsgebied('Strafrecht_Penitentiair strafrecht', 'Strafrecht')
    process_rechtsgebied('Strafrecht_Strafprocesrecht', 'Strafrecht')

    process_rechtsgebied('Internationaal publiekrecht', 'Internationaal publiekrecht')
    process_rechtsgebied('Internationaal publiekrecht_Mensenrechten', 'Internationaal publiekrecht')
    process_rechtsgebied('Internationaal publiekrecht_Volkenrecht', 'Internationaal publiekrecht')

