import sys
sys.path.insert(0, "../app/")
from app import app

class TestViewsGet:

    def setup_method(self):
        #print('before')
        app.testing = True
        self.client = app.test_client()

# find: button_NEW, button_CHANGES
    def test_get_home(self):
        response = self.client.get('/')
        data = response.data.decode()
        find_button_NEW = data.find('Submit new item')
        find_button_CHANGES = data.find('Submit new item')
        assert find_button_NEW != -1
        assert find_button_CHANGES != -1

# find: prometheus-metric version
    def test_get_metrics(self):
        response = self.client.get('/metrics')
        data = response.data.decode()
        find_VERSION = data.find('flask_exporter_info')
        assert find_VERSION != -1

    def teardown_method(self):
        pass

class TestViewsPost:

    def setup_method(self):
        #print('before')
        app.testing = True
        self.client = app.test_client()

    def test_post_home_add_item(self):
        text = {'todo_item': 'TEST.ADD_NEW_STRING'}
        response = self.client.post('/add', data=text)
        assert response.status_code == 302

    def test_post_home_delete_item(self):
        text = {'todo_item2': 'TEST.ADD_NEW_STRING'}
        response = self.client.post('/delete', data=text)
        assert response.status_code == 302

    def teardown_method(self):
        pass
