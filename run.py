from application import application
from flask import url_for

__author__ = 'elhe'

application.debug = True
application.run(port=8080)

url_for('static', filename='style.css')