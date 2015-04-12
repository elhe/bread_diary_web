from application import application, utils

from application.urls import DIARY_ADD_URL
from flask import render_template, request


__author__ = 'elhe'


@application.route('/', methods=['GET', ])
def index():
    return render_template('index.html')


@application.route('/add_food_entry', methods=['POST', 'GET'])
def add_food_entry():
    if request.method == 'POST':
        data = dict(name=request.form.get('food'),
                    width=request.form.get('weight'))
        application.logger.debug(data)
        response = utils.send_json_request('post', DIARY_ADD_URL, data)
        if response.status_code != 200:
            return render_template('index.html', message='FAILS')
    return render_template('index.html', message='OK')