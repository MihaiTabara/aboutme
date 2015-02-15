import flask

from .views import portal

DEFAULT_CONFIG = {
    'DEBUG': True,
}


def create_app(config={}):
    app = flask.Flask(__name__,
                      instance_relative_config=True)
    app.config.update(DEFAULT_CONFIG)
    app.config.from_pyfile('settings.py', silent=True)
    app.config.update(config)

    app.register_blueprint(portal)

    @app.route('/crashme')
    def crashme():
        raise RuntimeError('Crashing, as requested.')

    @app.route('/')
    def index():
        return 'Successful index page'

    return app
