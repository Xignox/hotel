from flask import Flask
from blueprints.backend import backend
from blueprints.frontend.login import login
from os.path import join, isfile
from extension import flask_login, db
from extension import  db




def create_app():
	app = Flask(__name__, instance_relative_config=True)
	
	#GoogleMaps(app, key="AIzaSyD1xXrHX2uNBdklKZyZymFvUp9AF9Hf0uo")
	
	if isfile(join('instance', 'settings.cfg')):
		app.config.from_pyfile('settings.cfg', silent=True)
	else:
		app.config.from_pyfile('settings.cfg', silent=True)


	app.register_blueprint(backend)
	
	app.register_blueprint(login)



	extensions(app)

	return app



def extensions(app):
    db.init_app(app)
    flask_login.init_app(app)

    return None

create_app().run(port=5000, debug=1)