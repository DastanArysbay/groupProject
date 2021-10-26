import os
import tempfile
import pytest
from flaskr import flaskr

@pytest.fixture
def client():
    db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    flaskr.app.config['TESTING'] = True

    with flaskr.app.test_client() as client:
        with flaskr.app.app_context():
            flaskr.init_db()
        yield client

    os.close(db_fd)
    os.unlink(flaskr.app.config['DATABASE'])



def login(client, login, password):
    return client.post('/singup/', data=dict(
        login=login,
        password=password
    ), follow_redirects=True)