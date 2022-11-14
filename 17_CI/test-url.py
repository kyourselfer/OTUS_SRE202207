#!/usr/bin/env python3
import pytest
import requests


@pytest.mark.parametrize("name,schema,url,port", [
    ("flask-sqlite3-todo-crud", "http://", "localhost", "5000"),
])
def test_access(host, name, schema, url, port):
    testedaddress = host.addr(url)
    res = testedaddress.is_resolvable
    por = testedaddress.port(port).is_reachable
    r = requests.get(schema + url + ":" + port)
    assert res == True
    assert por == True
    assert r.status_code == 200
