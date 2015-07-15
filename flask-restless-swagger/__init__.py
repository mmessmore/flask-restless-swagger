__author__ = 'Michael Messmore'
__email__ = 'mike@messmore.org'
__version__ = '0.1.0'


from flask import current_app

class SwagAPIManager(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)


    def init_app(self, app):
