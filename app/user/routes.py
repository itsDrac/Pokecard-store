from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app.user import user
from app.user.models import User
from app.user.forms import SignupForm, LoginForm

@user.route('/signup', methods = ['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        user.save()
        return form.data
    return render_template('signup.html', form=form)

@user.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects.filter(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            flash("LogIn successful","success")
        else :
            flash("Incorrect credentials, Try again","error")
    return render_template('login.html', form=form)

@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))
