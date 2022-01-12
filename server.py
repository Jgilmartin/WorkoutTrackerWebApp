from flask import Flask, render_template, redirect, url_for, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, login_user, LoginManager, UserMixin, logout_user

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.secret_key = 'secret-key'


class Users(UserMixin,db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String, unique=True, nullable=False) 
    password = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self): 
        return '<Users %r>' % self.username

    def checkPassword(self,password):
        return self.password == password


@login_manager.user_loader
def load_user(id):
    print()
    return Users.query.get(id)


@app.route('/')
def index():
    print('landing')
    if(not current_user.is_authenticated):
        print('not_auth')
        return redirect(url_for('login'))
    print('authenticated')
    return render_template('login.html')


@app.route('/login', methods =['GET','POST'], endpoint='login')
def Login():
    print('postLogin')
    if request.method == 'GET':
        if(current_user.is_authenticated):
            return redirect(url_for('studentView.html'))
        return render_template('login.html')

    if request.method == 'POST':
        print(request.form['username'])
        user = Users.query.filter_by(username = request.form['username'])
        if user is None:
            return redirect(url_for('login'))
        
        user = user.first()
        
        if user is None:
            return redirect(url_for('login'))

        if not user.checkPassword(request.form['password']):
            return redirect(url_for('login'))

        login_user(user)
        print (user.userLevel)
        return render_template('studentView.html',userid = user.id)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
