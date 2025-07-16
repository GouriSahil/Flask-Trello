from flask import render_template, url_for, redirect, flash
from flask_login import current_user, login_user, login_required, logout_user
from . import app, bcrypt, db
from .auth import RegestrationForm, LoginForm
from .models import User


@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegestrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash("Your account created successfully", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login success", "success")
            return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", 'success')
    return redirect(url_for('home'))
