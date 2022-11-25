import time, pytest, requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Uses Pytest to check basic checks
# Check: DNS is existed, port is reached and got 200 answer
@pytest.mark.parametrize("name,url,port", [
    ("db_access", "pg-0", "5432"),
    ("back-flask_access", "back-flask", "5000"),
    ("front-nginx_access", "front-nginx", "80"),
])
def test_svc_port_access(host, name, url, port):
    testedaddress = host.addr(url)
    resolve = testedaddress.is_resolvable
    portavail = testedaddress.port(port).is_reachable
    assert resolve == True
    assert portavail == True

@pytest.mark.parametrize("name,schema,url,port", [
    ("front-nginx_access", "http://", "front-nginx", "80"),
])
def test_svc_http_code_access(host, name, schema, url, port):
    response = requests.get(schema + url + ":" + port)
    assert response.status_code == 200

# Uses Selenium.webdriver.chrome
class TestUI:
    def test_uses_Chrome(url: str):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        options.add_argument('--start-maximized')

        driver = webdriver.Chrome(options=options)
        try:
            driver.get(url)
            time.sleep(2)

            # Try to match html title
            assert "Title" in driver.title
            # Try to find html body
            body = driver.find_element(By.TAG_NAME, 'body')
            assert body.is_displayed() == True
            # Try to find 1-st class name
            form1 = driver.find_element(By.CLASS_NAME, "make-todo");
            assert form1.is_displayed() == True
            # Try to find 2-nd class name
            form2 = driver.find_element(By.CLASS_NAME, 'delete-todo')
            assert form2.is_displayed() == True
        except Exception:
            pass
        finally:
            driver.close()
            driver.quit()

    if __name__ == "__main__":
        test_uses_Chrome("http://front-nginx")
