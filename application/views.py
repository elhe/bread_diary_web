from application import application, utils

from application.urls import DIARY_ADD_URL, DIARY_ALL_URL
from dateutil.parser import parser
from flask import render_template, request, url_for
from werkzeug.utils import redirect


__author__ = 'elhe'


@application.route('/', methods=['GET', ])
def index():
    response = utils.send_http_request('get', DIARY_ALL_URL)
    data = response.json()
    for entry in data['entries']:
        date_time = parser().parse(entry['date_time'])
        entry['date_time'] = date_time.strftime('%d.%m %H:%M')
    return render_template('index.html', entries=data['entries'])


@application.route('/add_food_entry', methods=['POST', 'GET'])
def add_food_entry():
    if request.method == 'POST':
        data = dict(name=request.form.get('food'),
                    width=request.form.get('weight'))

        response = utils.send_json_request('post', DIARY_ADD_URL, data)
        if response.status_code != 200:
            return render_template('index.html', message='FAILS')
    return redirect(url_for('index'))
