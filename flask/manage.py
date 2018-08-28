# manage.py

import os
import unittest
import coverage

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

COV = coverage.coverage(
    branch=True,
    include='gurdjieff/*',
    omit=[
        'gurdjieff/tests/*',
        'gurdjieff/config.py',
        'gurdjieff/*/__init__.py'
    ]
)
COV.start()

from gurdjieff import app, db
from gurdjieff.models import User

migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('gurdjieff/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('gurdjieff/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1

@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()

@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()

@manager.command
def create_admin():
    """Creates the admin user."""
    db.session.add(User(email='ad@min.com', password='admin', admin=True))
    db.session.commit()

@manager.command
def create_data():
    """Creates sample data."""
    pass

@manager.command
def preproc():
    """Preprocessor."""
    import rechtspraak.opendata.preprocess
    rechtspraak.opendata.preprocess.process_zip_to_xml('201112.zip')
    rechtspraak.opendata.preprocess.process_xml_to_db('2011')

@manager.command
def preproc_rechtsgebieden():
    """Rechtsgebieden preprocessor."""
    import rechtspraak.opendata.preprocess_rechtsgebieden
    rechtspraak.opendata.preprocess_rechtsgebieden.process_rechtsgebieden()

if __name__ == '__main__':
    manager.run()
