# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, url_for, json
from project import app, db
from project.models import Uitspraak

def process_to_db(json_str):

    uitspraken_dir = 'rechtspraak/opendata/uitspraken'
    year = '2010'
    d = open(os.path.join(uitspraken_dir, year, json_str), "r")
    data = json.load(d)

    #print(data['open-rechtspraak']['RDF']['Description'])

    data_root = data['open-rechtspraak']['RDF']['Description']
    identifier = data_root['identifier'].get('text')
    print("DEBUG: Identifier: %s" % identifier)

    # add to db
    u = Uitspraak(identifier)
    exists = db.session.query(Uitspraak.id).filter_by(identifier=identifier).scalar() is not None
    if not exists:
        db.session.add(u)
        db.session.commit()
