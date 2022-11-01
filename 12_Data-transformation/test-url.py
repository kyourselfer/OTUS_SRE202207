import pytest
import requests

@pytest.mark.parametrize("name,schema,url,port", [
    ("open-notify.org", "http://", "api.open-notify.org", "80"),
    ("flask-sqlite3-todo-crud", "http://", "localhost", "5000"),
])

def test_access(host, name, schema, url, port):
    testedaddress = host.addr(url)
    testedaddress.is_resolvable
    testedaddress.port(port).is_reachable
    r = requests.get(schema+url+":"+port)
    assert testedaddress.port
    assert testedaddress.is_resolvable
    assert r.status_code == 200