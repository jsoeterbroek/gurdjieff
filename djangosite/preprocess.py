# -*- coding: utf-8 -*-
import os,sys
from lxml import etree

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
from app.models import Uitspraak

#FIXME
#      later: after development

def process_zip_to_xml(zip):
    pass

def process_xml_to_db(year):
    """Parse all xml files for a give year and add to DB"""

    _dir = os.path.join('rechtspraak/opendata/uitspraken', year) 

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
                q = Uitspraak.objects.filter(description_identifier=description_identifier)
                if not q:
                    u = Uitspraak(
                            description_identifier=description_identifier,
                            description_format=description_format,
                            description_accessrights=description_accessrights,
                            description_modified=description_modified,
                            description_publicatiedatum=description_publicatiedatum,
                            description_language=description_language,
                            description_uitspraakdatum=description_uitspraakdatum,
                            description_zaaknummer=description_zaaknummer
                        )
                    u.save()

if __name__ == "__main__":
    process_xml_to_db('2006')
