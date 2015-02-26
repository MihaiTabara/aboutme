from flask import Flask, url_for, redirect
from application.views import portal

DEFAULT_CONFIG = {
    'DEBUG': True,
}


def create_app(config={}):
    app = Flask(__name__,
                instance_relative_config=True)
    app.config.update(DEFAULT_CONFIG)
    app.config.from_pyfile('settings.py', silent=True)
    app.config.update(config)

    app.register_blueprint(portal)

    if app.config.get('SENTRY_DSN'):
        from raven.contrib.flask import Sentry
        Sentry(app)

    @app.route('/crashme')
    def crashme():
        raise RuntimeError('Crashing, as requested.')

    @app.route('/')
    def index():
        return redirect(url_for('portal.aboutme'))

    return app
