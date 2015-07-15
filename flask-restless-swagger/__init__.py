__author__ = 'Michael Messmore'
__email__ = 'mike@messmore.org'
__version__ = '0.1.0'


from flask_restless import APIManager
from flask_restless.helpers import *
import yaml
import json

postgres_swagger = {
    'INTEGER': 'integer',
    'VARCHAR': 'string',
    'TEXT': 'string',
    'DATE': 'date',
    'BOOLEAN': 'bool',
    'BLOB': 'string'
}


class SwagAPIManager(object):
    swagger = {
        'swagger': '2.0',
        'info': {},
        'schemes': ['https'],
        'basePath': '/',
        'consumes': ['application/json'],
        'produces': ['application/json'],
        'paths': {},
        'definitions': {}
    }

    def __init__(self, app=None):
        self.app = None
        self.manager = None

        if app is not None:
            self.init_app(app)

    def to_json(self, **kwargs):
        return json.dumps(self.swagger, **kwargs)

    def to_yaml(self, **kwargs):
        return yaml.dump(self.swagger, **kwargs)

    # Try to be as much of a dict as possible
    def __getitem__(self, item):
        return self.swagger[item]

    def __setitem__(self, key, value):
        self.swagger[key] = value

    def __delitem__(self, key):
        del (self.swagger[key])

    def __contains__(self, item):
        return item in self.swagger

    def __len__(self):
        return len(self.swagger)

    def __str__(self):
        return self.to_json(indent=4)

    @property
    def version(self):
        if 'version' in self.swagger['info']:
            return self.swagger['info']['version']
        return None

    @version.setter
    def version(self, value):
        self.swagger['info']['version'] = value

    @property
    def title(self):
        if 'title' in self.swagger['info']:
            return self.swagger['info']['title']
        return None

    @title.setter
    def title(self, value):
        self.swagger['info']['title'] = value

    @property
    def description(self):
        if 'description' in self.swagger['info']:
            return self.swagger['info']['description']
        return None

    @description.setter
    def description(self, value):
        self.swagger['info']['description'] = value

    def add_path(self, model, **kwargs):
        name = model.__tablename__
        schema = model.__name__
        path = kwargs.get('url_prefix', ""), '/' + name
        self.swagger['paths'][path] = {}

        for method in [m.lower() for m in kwargs.get('methods', ['GET'])]:
            if method == 'get':
                self.swagger['paths'][path][method] = {
                    'parameters': [{
                        'name': 'q',
                        'in': 'query',
                        'description': 'searchjson',
                        'type': 'string'
                    }],
                    'responses': {
                        200: {
                            'description': 'List ' + name,
                            'schema': {
                                'title': name,
                                'type': 'array',
                                'items': {'$ref': '#/definitions/' + name}
                            }
                        }

                    }
                }
                self.swagger['paths']["{}/{{{}Id}}".format(path, schema.lower())][method] = {
                    'parameters': [{
                        'name': schema.lower() + 'Id',
                        'in': 'path',
                        'description': 'ID of ' + schema,
                        'required': True,
                        'type': 'integer'
                    }],
                    'responses': {
                        200: {
                            'description': 'Success ' + name,
                            'schema': {
                                'title': name,
                                '$ref': '#/definitions/' + name
                            }
                        }

                    }
                }
            elif method == 'delete':
                self.swagger['paths']["{}/{{{}Id}}".format(path, schema.lower())][method] = {
                    'parameters': [{
                        'name': schema.lower() + 'Id',
                        'in': 'path',
                        'description': 'ID of ' + schema,
                        'required': True,
                        'type': 'integer'
                    }],
                    'responses': {
                        200: {
                            'description': 'Success'
                        }

                    }
                }
            else:
                self.swagger['paths'][path][method] = {
                    'parameters': [{
                        'name': name,
                        'in': 'body',
                        'description': schema,
                        'type': "#/definitions/" + schema
                    }],
                    'responses': {
                        200: {
                            'description': 'Success'
                        }

                    }
                }

    def add_defn(self, model, **kwargs):
        name = model.__name__
        self.swagger['definitions'][name] = {
            'type': 'object',
            'properties': {}
        }
        columns = get_columns(model).keys()
        for column_name, column in get_columns(model).iteritems():
            if column_name in kwargs.get('exclude_columns'):
                continue
            try:
                column_defn = postgres_swagger[column.type]
            except AttributeError:
                schema = get_related_model(model, column_name)
                if column_name + '_id' in columns:
                    column_defn = {'schema': {
                        '$ref': schema.__name__
                    }}
                else:
                    column_defn = {'schema': {
                        'type': 'array',
                        'items': {
                            '$ref': schema.__name__
                        }
                    }}
            self.swagger['definitions'][name]['properties'][column_name] = column_defn

    def init_app(self, app):
        self.app = app

    def init_manager(self, db):
        self.manager = APIManager(self.app, flask_sqlalchemy_db=db)

    def create_api(self, model, **kwargs):

        self.manager.create_api(model, **kwargs)
