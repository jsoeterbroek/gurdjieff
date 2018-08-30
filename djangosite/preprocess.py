# -*- coding: utf-8 -*-
import os
from lxml import etree
from flask import Flask, render_template, url_for, json
from gurdjieff import app, db
from gurdjieff.models import Uitspraak

#FIXME
#      later: after development
def process_zip_to_xml(zip):
    pass

def process_xml_to_db(year):
    """Parse all xml files for a give year and add to DB"""

    _dir = os.path.join('rechtspraak/opendata/uitspraken', year) 
    print(_dir)

    # namespaces map
    nsmap = {
        'dcterms': 'http://purl.org/dc/terms/',
        'psi': 'http://psi.rechtspraak.nl/',
        'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
    }

    for _file in os.listdir(_dir):
        if 'xml' in _file:
            _f = os.path.join(_dir, _file) 
            print("INFO: parsing %s" % _f)
            with open(_f, 'r', encoding="utf-8") as content:

                #TODO: Do not parse xml if allready parsed (touchfile?)
                #      later: after development

                tree = etree.parse(content)
                root = tree.getroot()

                # 4 delen
                #
                # 1.) <rdf:RDF/rdf:Description
                # 1.1.) <dcterms:identifier>
                a = root.xpath('rdf:RDF/rdf:Description/dcterms:identifier', namespaces=nsmap)
                element = a[0] if a else None
                description_identifier = element.text
                # 1.2.) <dcterms:format>
                a = root.xpath('rdf:RDF/rdf:Description/dcterms:format', namespaces=nsmap)
                element = a[0] if a else None
                description_format = element.text
                # 1.3.) <dcterms:accessRights>
                a = root.xpath('rdf:RDF/rdf:Description/dcterms:accessRights', namespaces=nsmap)
                element = a[0] if a else None
                description_accessrights = element.text
                # 1.4.) <dcterms:modified>
                a = root.xpath('rdf:RDF/rdf:Description/dcterms:modified', namespaces=nsmap)
                element = a[0] if a else None
                description_modified = element.text
                # 1.5.) <dcterms:issued rdfs:label="Publicatiedatum">
                a = root.xpath('rdf:RDF/rdf:Description/dcterms:issued', namespaces=nsmap)
                element = a[0] if a else None
                description_publicatiedatum = element.text

                # 1.6.) <dcterms:publisher>

                # 1.7.) <dcterms:language>
                a = root.xpath('rdf:RDF/rdf:Description/dcterms:language', namespaces=nsmap)
                element = a[0] if a else None
                description_language = element.text

                # subject/rechtsgebied
                a = root.xpath('rdf:RDF/rdf:Description/dcterms:subject', namespaces=nsmap)
                if a:
                    element = a[0]
                    description_rechtsgebied = element.text
                else:
                    description_rechtsgebied = 'Onbekend'

                description_uitspraakdatum = 'foo' #FIXME

                #description_zaaknummer
                a = root.xpath('rdf:RDF/rdf:Description/psi:zaaknummer', namespaces=nsmap)
                if a:
                    element = a[0]
                    description_zaaknummer = element.text
                else:
                    description_zaaknummer = 'Geen/Onbekend'



                #2) <rdf:RDF/rdf:Description rdf:about=
                #3) <inhoudsindicatie
                #4) <uitspraak

                # add and commit to db
                u = Uitspraak(
                        description_identifier,
                        description_format,
                        description_accessrights,
                        description_modified,
                        description_publicatiedatum,
                        description_language,
                        description_rechtsgebied,
                        description_uitspraakdatum,
                        description_zaaknummer
                        )
                exists = db.session.query(Uitspraak.id).filter_by(description_identifier=description_identifier).scalar() is not None
                if not exists:
                    db.session.add(u)
                    db.session.commit()
