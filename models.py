

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dastanio2020@localhost/ass3' # не забудь менять имя датабэйс и пароль 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class UserTable(db.Model):
    __tablename__ = 'usertable'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column( db.String(255))
    password = db.Column( db.String(255))
    token = db.Column( db.String(255))

  
    def __init__(self,id,login, password, token):
        self.id = id
        self.login = login
        self.password = password
        self.token = token

#Удаляем таблицу, если существует
db.engine.execute('drop table IF EXISTS usertable')
#Создаем таблицу заново
db.engine.execute('CREATE TABLE usertable (ID int, login VARCHAR (255), password VARCHAR (255), token VARCHAR (255), PRIMARY KEY (ID))')
#Наполняем таблицу пятью строками
new_ex = UserTable(5,'Fillizeni@gmail.com', 'dastan', 'token')
db.session.add(new_ex)
new_ex = UserTable(4,'Ainur@gmail.com', 'asdfghjk', 'token')
db.session.add(new_ex)
new_ex = UserTable(3,'Kanat@gmail.ru', 'asd123', 'token')
db.session.add(new_ex)
new_ex = UserTable(2,'Ashat@mail.ru', 'iloveyou', 'token')
db.session.add(new_ex)
new_ex = UserTable(1,'das@mail.ru', 'qwerty', 'token')
db.session.add(new_ex)

db.session.commit()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dastanio2020@localhost/ass3' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    def ping_pong():
        return jsonify({
            'status': 'Epic success',
            'message': 'pong!'
        })
    return app
    

