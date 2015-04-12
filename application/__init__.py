from flask import Flask

__author__ = 'elhe'

application = Flask(__name__)
from application import views

