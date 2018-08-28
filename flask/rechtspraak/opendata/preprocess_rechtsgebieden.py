# -*- coding: utf-8 -*-
# gurdjieff/models.py
import datetime
from gurdjieff import app, db, bcrypt
from gurdjieff.models import Hoofdrechtsgebied, Rechtsgebied

def process_hoofdrechtsgebied(hoofdrechtsgebied):
    #d = db.session.query(hoofdrechtsgebied).filter_by(naam=hoofdrechtsgebied).first()
    #if d:
    #    db.session.delete(d)
    u = Hoofdrechtsgebied(hoofdrechtsgebied)
    db.session.add(u)
    db.session.commit()

def process_rechtsgebied(rechtsgebied,hoofdrechtsgebied):
    #d = db.session.query(Rechtsgebied).filter_by(naam=rechtsgebied).first()
    #if d:
    #    db.session.delete(d)
    u = Rechtsgebied(rechtsgebied)
    h = db.session.query(Hoofdrechtsgebied).filter_by(naam=hoofdrechtsgebied).first()
    db.session.add(u)
    h.subs.append(u)
    db.session.commit()

def process_rechtsgebieden():
    process_hoofdrechtsgebied('Bestuursrecht')
    process_hoofdrechtsgebied('Civiel recht')
    process_hoofdrechtsgebied('Strafrecht')
    process_hoofdrechtsgebied('Internationaal publiekrecht')
   
    process_rechtsgebied('Ambtenarenrecht', 'Bestuursrecht')
    process_rechtsgebied('Belastingrecht', 'Bestuursrecht')
    process_rechtsgebied('Bestuursprocesrecht', 'Bestuursrecht')
    process_rechtsgebied('Bestuursstrafrecht', 'Bestuursrecht')
    process_rechtsgebied('Europees bestuursrecht', 'Bestuursrecht')
    process_rechtsgebied('Mededingingsrecht', 'Bestuursrecht')
    process_rechtsgebied('Omgevingsrecht', 'Bestuursrecht')
    process_rechtsgebied('Socialezekerheidsrecht', 'Bestuursrecht')
    process_rechtsgebied('Vreemdelingenrecht', 'Bestuursrecht')
    
    process_rechtsgebied('Aanbestedingsrecht', 'Civiel recht')
    process_rechtsgebied('Arbeidsrecht', 'Civiel recht')
    process_rechtsgebied('Burgerlijk procesrecht', 'Civiel recht')
    process_rechtsgebied('Europees civiel recht', 'Civiel recht')
    process_rechtsgebied('Goederenrecht', 'Civiel recht')
    process_rechtsgebied('Insolventierecht', 'Civiel recht')
    process_rechtsgebied('Intellectueel-eigendomsrecht', 'Civiel recht')
    process_rechtsgebied('Internationaal privaatrecht', 'Civiel recht')
    process_rechtsgebied('Mededingingsrecht', 'Civiel recht')
    process_rechtsgebied('Ondernemingsrecht', 'Civiel recht')
    process_rechtsgebied('Personen- en familierecht', 'Civiel recht')
    process_rechtsgebied('Verbintenissenrecht', 'Civiel recht')

    process_rechtsgebied('Europees strafrecht', 'Strafrecht')
    process_rechtsgebied('Internationaal strafrecht', 'Strafrecht')
    process_rechtsgebied('Materieel strafrecht', 'Strafrecht')
    process_rechtsgebied('Penitentiair strafrecht', 'Strafrecht')
    process_rechtsgebied('Strafprocesrecht', 'Strafrecht')

    process_rechtsgebied('Mensenrechten', 'Internationaal publiekrecht')
    process_rechtsgebied('Volkenrecht', 'Internationaal publiekrecht')

