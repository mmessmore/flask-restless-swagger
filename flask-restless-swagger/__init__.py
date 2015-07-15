__author__ = 'Michael Messmore'
__email__ = 'mike@messmore.org'
__version__ = '0.1.0'


from flask import current_app
from flask_restless import APIManager

class SwagAPIManager(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)


    def init_app(self, app):
        self.app = app

    def init_manager(self, db):
        self.manager = flask.ext.restless.APIManager(self.app,
                                                     flask_sqlalchemy_db=db)
