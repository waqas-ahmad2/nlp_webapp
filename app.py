from flask import Flask, render_template,request,redirect,session,url_for
from db import Database
from api import API

app = Flask(__name__)
dbo = Database()
apio = API()
app.config['SECRET_KEY'] = 'Super_Secret_Key'



@app.route('/')
def index():
    return render_template('Landing_page.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    username = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.create_data(username,email,password)

    if response:
        return render_template('login.html', msg='Registration Sucessful')
    else:
        return render_template('register.html', msg='Email Already Exists')


@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.search_data(email,password)


    if response:
        user = dbo.get_user_name(email,password).capitalize()
        session['user'] = user
        print(session)
        return render_template('profile.html')
    else:
        return render_template('login.html', txt = 'invalid email/password combination')


@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return render_template('login.html')

@app.route('/ner_profile')
def ner_profile():
    if session:
        return render_template('ner_profile.html')
    else:
        return render_template('login.html')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    if session:
        text = request.form.get('txtbox')
        response = apio.ner_analysis(text)
        return render_template('ner_profile.html', msg = response)
    else:
        return render_template('login.html')

@app.route('/sentiments_profile')
def sentiments_profile():
    if session:
        return render_template('sentiments_profile.html')
    else:
        return render_template('login.html')

@app.route('/perform_sentiments', methods=['post'])
def perform_sentiments():
    if session:
        text = request.form.get('txtbox')
        response = apio.sentiments_analysis(text)
        return render_template('sentiments_profile.html', msg = response)
    else:
        return render_template('login.html')

@app.route('/emotions_profile')
def emotions_profile():
    if session:
        return render_template('/emotions_profile.html')
    else:
        return render_template('login.html')


@app.route('/perform_emotions',methods=['post'])
def perform_emotions():
    if session:
        text = request.form.get('txtbox')
        response = apio.emotions_analysis(text)
        return render_template('/emotions_profile.html', msg = response)
    else:
        return render_template('login.html')


@app.route('/perform_logout')
def logout():
    if session:
        session.pop('user')
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

# if __name__ == '__main__':
app.run(debug=True)
