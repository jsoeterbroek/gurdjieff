# -*- coding: utf-8 -*-
# project/models.py
import datetime
from project import app, db, bcrypt

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

class Uitspraak(db.Model):

    __tablename__ = "uitspraak"

    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    registered_on   = db.Column(db.DateTime, nullable=False)
    identifier      = db.Column(db.String(25), default = '', unique=True)
    modified        = db.Column(db.String(255), nullable=False)
    publicatiedatum = db.Column(db.String(255), nullable=False)
    uitspraakdatum  = db.Column(db.String(255), nullable=False)

    def __init__(self, identifier = '', modified, publicatiedatum, uitspraakdatum):
        self.registered_on   = datetime.datetime.now()
        self.identifier      = identifier
        self.modified        = modified
        self.publicatiedatum = publicatiedatum
        self.uitspraakdatum  = uitspraakdatum

    def get_id(self):
        return self.id

    def get_modified(self):
        return self.modified

    def get_publicatiedatum(self):
        return self.publicatiedatum

    def get_uitspraakdatum(self):
        return self.uitspraakdatum

    def __repr__(self):
        return '<Identifier {0}>'.format(self.identifier)

