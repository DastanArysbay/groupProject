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
        string = "Well done! Succsessfully added token on database"
        update_this = UserTable.query.filter_by(login=login, password=password).first()
        update_this.token = token
        #Заносим токен в базу данных. Обновляем занчение в колонне token в той строке, где записанный логин равен введенному логину
        db.engine.execute('''update usertable set token = {} where login= '{}'  '''.format( 'token', auth.username))
        db.session.commit()
        return jsonify(string)
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})


@app.route('/protected')
def protection():
    #Получаем токен из URL
    token = request.args.get('token')
    #Проверяем с теми токенами, что есть в таблице
    #Если не совпадает ни с одним значением, то выводится ответ 'Hello, Could not verify the token: token'
    user = UserTable.query.filter_by(token=token).first_or_404(description='Hello, Could not verify the token:  {}'.format(token))
    #Если совпадает с токеном, что есть в таблице, то выводит этот ответ
    return '''<h1>Hello, token which is provided is correct</h1> '''.format(token)


if __name__ == '__main__':
    app.run(debug=True)
