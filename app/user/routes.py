from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from app.user import user_bp as u
from app.user.models import User
from app.user.forms import SignupForm, LoginForm
from app.product.models import Product

@u.route('/signup', methods = ['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        user.save()
        return form.data
    return render_template('signup.html', form=form)

@u.route('/login', methods = ['GET','POST'])
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

@u.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user_bp.login'))

@u.get('/cart')
@login_required
def cart():
    return render_template('cart.html', cart=current_user.cart)

@u.get('/update_cart/<int:p_no>')
@login_required
def update_cart(p_no):
    prod = Product.objects.filter(no=p_no).first()
    p = current_user.cart.filter(product=prod).first()
    val = request.args.get('val',1,int)
    print("-->",p,val)
    if val == 1:
        if not p:
            current_user.cart.create(product=prod)
    if val == 2:
        if p:
            p.quntity += 1
    if val == 3:
        if p:
            p.quntity -= 1
    if val == 4:
        if p:
           current_user.cart.remove(p) 
    print(current_user.cart)
    current_user.save()
    return redirect(url_for('user_bp.cart'))
