# gurdjieff/__init__.py


#################
#### imports ####
#################

import os

from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


################
#### config ####
################

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)


app_settings = os.getenv('APP_SETTINGS', 'gurdjieff.config.DevelopmentConfig')
app.config.from_object(app_settings)

####################
#### extensions ####
####################

login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
toolbar = DebugToolbarExtension(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

####################
#### models ########
####################

from gurdjieff.models import User
from gurdjieff.models import Uitspraak, UitspraakAdminView
from gurdjieff.models import Rechtsgebied

###################
### admin #########
###################

admin = Admin(app, name='gurdjieff', template_mode='bootstrap3')
admin.add_view(UitspraakAdminView(Uitspraak, db.session))
admin.add_view(ModelView(Rechtsgebied, db.session))

###################
### blueprints ####
###################

from gurdjieff.user.views import user_blueprint
from gurdjieff.main.views import main_blueprint
app.register_blueprint(user_blueprint)
app.register_blueprint(main_blueprint)

###################
### flask-login ###
###################

login_manager.login_view = "user.login"
login_manager.login_message_category = 'danger'

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

########################
#### error handlers ####
########################

@app.errorhandler(401)
def unauthorized_page(error):
    return render_template("errors/401.html"), 401

@app.errorhandler(403)
def forbidden_page(error):
    return render_template("errors/403.html"), 403

@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404

@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500
