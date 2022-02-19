from flask import render_template
from app.user import user
from app.user.models import User
from app.user.forms import SignupForm

@user.route('/signup', methods = ['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        user.save()
        return form.data
    return render_template('signup.html', form=form)
