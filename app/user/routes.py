from flask import render_template
from app.user import user
from app.user.forms import SignupForm

@user.route('/signup', methods = ['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        return form.data
    return render_template('signup.html', form=form)
