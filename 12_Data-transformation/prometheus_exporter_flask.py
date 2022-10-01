import prometheus_client
import werkzeug
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import flask
import random
import time

SERVICE_UPTIME = prometheus_client.Gauge('service_uptime',
                                         'Hold the time elasted since service startup')
RESPONSE_TIME = prometheus_client.Gauge('response_time_last',
                                        'Hold the last request response time')

# Create Flask app
app = flask.Flask(__name__)


@app.route('/')
@RESPONSE_TIME.time()
def hello():
    time.sleep(random.random())
    return "Hello World!"


# Add prometheus wsgi middleware to route /metrics requests
app_dispatch = werkzeug.middleware.dispatcher.DispatcherMiddleware(app, {'/metrics': prometheus_client.make_wsgi_app()})

# BASH
# uwsgi --http 127.0.0.1:9999 --wsgi-file prometheus_exporter_flask.py --callable app_dispatch