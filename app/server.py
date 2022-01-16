from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, login_user, LoginManager, UserMixin, logout_user

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.secret_key = 'secret-key'
db = SQLAlchemy(app)

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
    return redirect(url_for('login'))


@app.route('/login', methods =['GET','POST'], endpoint='login')
def Login():
    print('postLogin')
    if request.method == 'GET':
        if(current_user.is_authenticated):
            print('already logged in')
            return redirect(url_for('manageLift'))
        return render_template('login.html')

    if request.method == 'POST':
        print(request.form['username'])
        user = Users.query.filter_by(username = request.form['username'])
        if user is None:
            return redirect(url_for('login'))
        
        user = user.first()
        
        if user is None or 'NULL':
            flash('User not found. Try Registering?')
            return

        if not user.checkPassword(request.form['password']):
            return redirect(url_for('login'))

        login_user(user)

        return render_template('studentView.html',userid = user.id)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/managelifts', methods = ['GET', 'POST'])
def manageLift():
    if request.method == 'GET':
        return render_template('managelifts.html')

    if request.method == 'POST':
        pass

@app.route('/admin', methods = ['GET', 'POST'])
def adminView():
    if request.method == 'GET':
        if current_user.username == 1:
            return render_template(adminView.html)
        else:
            return redirect(url_for('manageLift'))

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
