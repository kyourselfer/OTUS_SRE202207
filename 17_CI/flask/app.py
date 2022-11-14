#!/usr/bin/env python3
import requests
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import prometheus_client
from prometheus_flask_exporter import PrometheusMetrics
import threading
import time

app = Flask(__name__)
metrics = PrometheusMetrics(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

# static information as metric
metrics.info('app_info', 'Application info', version='0.0.1')

SERVICE_UPTIME = prometheus_client.Gauge('service_uptime',
                                         'Hold the time elasted since service startup')
RESPONSE_TIME = prometheus_client.Gauge('response_time_last',
                                        'Hold the last request response time')

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

@app.route("/", methods=["GET","HEAD"])
@RESPONSE_TIME.time()
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@app.route('/add', methods=["POST"])
def add():
    data = request.form["todo_item"]
    todo = Todo(text=data, complete=False)
    db.session.add(todo)
    db.session.commit()
    # return data # DEBUG REQUEST
    return redirect(url_for("index"))

@app.route('/update', methods=["POST"])
def update():
    # return request.form # DEBUG REQUEST
    return redirect(url_for("index"))

@app.route("/metrics", methods=["GET"])
@metrics.do_not_track()
def metrics():
    # Add prometheus wsgi middleware to route /metrics requests
    return prometheus_client.make_wsgi_app()

# Parsing WebAPI. https://www.youtube.com/watch?v=mNJKCg4BjC8
@app.route("/api", methods=["GET"])
def api():
    # Convert html output GET, POST to Json API?
    app_api = requests.get('http://localhost:5000/',)
    #app_api = requests.get('http://api.open-notify.org/iss-now.json')
    #print(app_api.status_code)
    app_api = app_api.text
    app_api = jsonify(app_api)
    return app_api

def update_uptime():
    while True:
        SERVICE_UPTIME.inc(1)
        time.sleep(1)

SERVICE_UPTIME.set(0)
uptime_updater = threading.Thread(target=update_uptime)
uptime_updater.start()


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, threaded=True, debug=False)
