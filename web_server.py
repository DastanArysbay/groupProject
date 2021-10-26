from datetime import datetime, timedelta
from flask import Flask
from flask.helpers import make_response
from flask import request
from flask.json import jsonify
from models import UserTable
from models import db, app
import jwt


app.config['SECRET_KEY'] = 'thisismyflasksecretkey'
@app.route('/signup/<login>/<password>')
def signup(login,password):
    auth = request.authorization
    user = UserTable.query.filter_by(login=login, password=password).first_or_404(description='Could not found a user with login and password:  {}'.format(login))
    if auth and auth.password == password and auth.username == login:
        token = jwt.encode({'user':auth.username, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
        string = "You are fu*king CRAZY_MAN! succsessfully added token on database"
        update_this = UserTable.query.filter_by(login=login, password=password).first()
        update_this.token = token
        db.session.commit()
        return jsonify(string)
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})

# Айым, вот часть про "protected", я пошел писать unittest
# @app.route('/protected')
# def protection():
#     token = request.args.get('token')
#     return '''<h1> The token is {} <h1>'''.format(token)


if __name__ == '__main__':
    app.run(debug=True)