=============================
flask-restless-swagger
=============================

.. image:: https://travis-ci.org/mmessmore/flask-restless-swagger.png?branch=master
    :target: https://travis-ci.org/mmessmore/flask-restless-swagger

.. image:: https://pypip.in/d/flask-restless-swagger/badge.png
    :target: https://pypi.python.org/pypi/flask-restless-swagger


Magically create Swagger_ documentation as you magically create your RESTful API with Flask-Restless_

This has lingered a while without the love it needs due to other more pressing projects.  Contributions are welcome and appreciated.

Features
--------

This strives to be a drop in replacement for Flask-Restless_' APIManager.  It wraps 
the APIManager calls to try to gather enough information to present a Swagger_ 2.0
file.  It also deploys the static content for the Swagger-UI configured to point
to said Swagger_ JSON file.

Status
------
Currently it "works-for-me".  There are a few terrible assumptions it makes.  It 
probably needs some more features to be usable for everyone.  Suggestions, and 
pull requests are welcome.

TODO
----

* Add Docstrings in Models as descriptions
* Cleanup Markup
* Make it suck less

.. _Flask-Restless: https://flask-restless.readthedocs.org/en/latest/
.. _Swagger: http://swagger.io

