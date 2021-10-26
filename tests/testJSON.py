import pytest
from flask import json, jsonify

@app.route('/signup/<login>')
def users_me():
    return jsonify(username=g.user.login)

with user_set(app, user):
    with app.test_client() as c:
        resp = c.get('/signup/<login>')
        data = json.loads(resp.data)
        self.assert_equal(data['login'], user.login)