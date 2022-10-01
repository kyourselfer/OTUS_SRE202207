import pytest
import requests

method="GET"
redirect="True"
timeout=3

@pytest.mark.parametrize("name,schema,url,port", [
    ("Google", "https://", "google.com", "443"),
    ("open-notify.org", "http://", "api.open-notify.org/iss-now.json", "80"),
])

def test_access(host, name, schema, url, port):
    testedaddress = host.addr(url)
    testedaddress.is_resolvable
    testedaddress.port(port).is_reachable
    response = requests.get(schema+url,port)
    assert response.status_code == 200

