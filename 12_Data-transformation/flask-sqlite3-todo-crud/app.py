from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import prometheus_client
from prometheus_client import metrics
from prometheus_flask_exporter import PrometheusMetrics
import werkzeug
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import threading
import time


app = Flask(__name__)
metrics = PrometheusMetrics(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

SERVICE_UPTIME = prometheus_client.Gauge('service_uptime',
                                         'Hold the time elasted since service startup')
RESPONSE_TIME = prometheus_client.Gauge('response_time_last',
                                        'Hold the last request response time')

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)


@app.route("/", methods=["HEAD", "OPTIONS", "GET"])
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
    app_dispatch = werkzeug.middleware.dispatcher.DispatcherMiddleware(app, {
        '/metrics': prometheus_client.make_wsgi_app()
    })
    return app_dispatch

def update_uptime():
    while True:
        SERVICE_UPTIME.inc(1)
        time.sleep(1)

SERVICE_UPTIME.set(0)
uptime_updater = threading.Thread(target=update_uptime)
uptime_updater.start()


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, threaded=True, debug=False)
