"""
Tests for `flask-restless-swagger` module.
"""

import flask_restless_swagger

def test_import():
    assert 'SwagAPIManager' in dir(flask_restless_swagger)
