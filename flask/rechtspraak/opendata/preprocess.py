# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, url_for, json
from gurdjieff import app, db
from gurdjieff.models import Uitspraak

def process_zip_to_xml(zip):
    pass

def process_xml_to_db(year):

    _dir = 'rechtspraak/opendata/uitspraken'
    print(_dir)
    #d = open(os.path.join(_dir, year, json_str), "r")

    #data = json.load(d)

    #print(data['open-rechtspraak']['RDF']['Description'])

    #data_root = data['open-rechtspraak']['RDF']['Description']
    #identifier = data_root['identifier'].get('text')
    ##print("DEBUG: Identifier: %s" % identifier)
    #modified = data_root['modified'].get('text')
    #publicatiedatum = data_root['issued'].get('text')
    #uitspraakdatum = data_root['date'].get('text')
    #zaaknummer = data_root['zaaknummer'].get('text')

    ## add and commit to db
    #u = Uitspraak(identifier, modified, publicatiedatum, uitspraakdatum, zaaknummer)
    #exists = db.session.query(Uitspraak.id).filter_by(identifier=identifier).scalar() is not None
    #if not exists:
    #    db.session.add(u)
    #    db.session.commit()
