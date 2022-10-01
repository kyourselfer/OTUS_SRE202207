import requests
import prometheus_client
import time


DEST_SCHEMA="http://"
DEST_URL="api.open-notify.org/iss-now.json"
DEST_PORT="80"

UPDATE_PERIOD = 3
ISS_TIME = prometheus_client.Gauge('iss_time',
                                       'Hold current time from ISS',
                                       ['resource_type'])
ISS_POSITION = prometheus_client.Gauge('iss_position',
                                       'Hold current position from ISS',
                                       ['resource_type'])
def get_body(DEST_SCHEMA, DEST_URL, DEST_PORT):
    response = requests.get(DEST_SCHEMA+DEST_URL,DEST_PORT)
    return response.json()
    #return response.headers['content-type']

if __name__ == '__main__':
    prometheus_client.start_http_server(9090)

# TODO: Metrics
while True:
    ISS_TIME.labels('timestamp').set(get_body(DEST_SCHEMA, DEST_URL, DEST_PORT)['timestamp'])
    iss_position = get_body(DEST_SCHEMA, DEST_URL, DEST_PORT)['iss_position']
    for itempo in iss_position.keys():
        ISS_POSITION.labels(itempo).set(iss_position[itempo])
    time.sleep(UPDATE_PERIOD)
