import threading
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

def update_uptime():
  while True:
    SERVICE_UPTIME.inc(1)
    time.sleep(1)

SERVICE_UPTIME.set(0)
uptime_updater = threading.Thread(target=update_uptime)
uptime_updater.start()


# BASH
# uwsgi --http 127.0.0.1:9090 --wsgi-file prometheus_exporter_flask.py --callable app_dispatch