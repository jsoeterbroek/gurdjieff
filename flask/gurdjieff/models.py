# -*- coding: utf-8 -*-
# gurdjieff/models.py
import datetime
from gurdjieff import app, db, bcrypt
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

class Uitspraak(db.Model):

    __tablename__ = "uitspraak"

    id                          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    registered                  = db.Column(db.String(25), nullable=False)
    description_identifier      = db.Column(db.String(25), unique=True, nullable=False)
    description_format          = db.Column(db.String(25), nullable=False)
    description_accessrights    = db.Column(db.String(25), nullable=False)
    description_modified        = db.Column(db.String(255), nullable=False)
    description_publicatiedatum = db.Column(db.String(255), nullable=False)
    description_language        = db.Column(db.String(25), nullable=False)
    description_rechtsgebied    = db.Column(db.String(255), nullable=False) # TODO relationship with Rechtsgebied
    description_uitspraakdatum  = db.Column(db.String(255), nullable=False)
    description_zaaknummer      = db.Column(db.String(255), nullable=False)

    def __init__(self,
            description_identifier,
            description_format,
            description_accessrights,
            description_modified,
            description_publicatiedatum,
            description_language,
            description_rechtsgebied,
            description_uitspraakdatum,
            description_zaaknummer,
        ):

        self.registered                  = datetime.datetime.now().strftime("%Y-%m-%d")
        self.description_identifier      = description_identifier
        self.description_format          = description_format
        self.description_accessrights    = description_accessrights
        self.description_modified        = description_modified
        self.description_publicatiedatum = description_publicatiedatum
        self.description_language        = description_language
        self.description_rechtsgebied    = description_rechtsgebied
        self.description_uitspraakdatum  = description_uitspraakdatum
        self.description_zaaknummer      = description_zaaknummer

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<Identifier {0}>'.format(self.description_identifier)

class UitspraakAdminView(ModelView):
    column_searchable_list = ('description_identifier',)
    column_labels = {
        'description_identifier': 'Identifier',
        'description_modified': 'Modified',
        'description_publicatiedatum': 'Publicatiedatum',
        'description_rechtsgebied': 'Rechtsgebied',
        'description_uitspraakdatum': 'Uitspraakdatum',
        'description_zaaknummer': 'Zaaknummer',
    }
    column_exclude_list = (
        'registered',
        'description_format',
        'description_accessrights',
        'description_modified',
        'description_language',
    )
    form_excluded_columns = (
        'registered',
        'description_format',
        'description_accessrights',
        'description_modified',
        'description_language',
    )
    column_display_actions = False
    column_details_list = None
    column_display_pk = True
    can_view_details = False

class Rechtsgebied(db.Model):

    __tablename__ = "rechtsgebied"

    id                    = db.Column(db.Integer, primary_key=True, autoincrement=True)
    naam                  = db.Column(db.String(55))

    def __init__(self, naam):
        self.naam = naam

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<Rechtsgebied {0}>'.format(self.naam)

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        )
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {0}>'.format(self.email)

