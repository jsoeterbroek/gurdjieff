# -*- coding: utf-8 -*-
import os
from lxml import etree
from flask import Flask, render_template, url_for, json
from gurdjieff import app, db
from gurdjieff.models import Uitspraak

def process_zip_to_xml(zip):
    pass

def process_xml_to_db(year):

    _dir = os.path.join('rechtspraak/opendata/uitspraken', year) 
    print(_dir)

    # namespaces map
    # xmlns:dcterms="http://purl.org/dc/terms/"
    # xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    nsmap = {
            'dcterms': 'http://purl.org/dc/terms/',
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
            }

    for _file in os.listdir(_dir):
        if 'xml' in _file:
            _f = os.path.join(_dir, _file) 
            print("INFO: parsing %s" % _f)
            with open(_f, 'r', encoding="utf-8") as content:
                tree = etree.parse(content)
                root = tree.getroot()

                lst_identifier = root.findall('.//dcterms:identifier', namespaces=nsmap)
                for l in lst_identifier:
                    identifier = l.text
                #print("DEBUG: Identifier: %s" % identifier)

                modified = 'foo' #FIXME
                publicatiedatum = 'foo' #FIXME
                uitspraakdatum = 'foo' #FIXME
                zaaknummer = 'foo' #FIXME

                # add and commit to db
                u = Uitspraak(identifier, modified, publicatiedatum, uitspraakdatum, zaaknummer)
                exists = db.session.query(Uitspraak.id).filter_by(identifier=identifier).scalar() is not None
                if not exists:
                    db.session.add(u)
                    db.session.commit()
