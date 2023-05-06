from flask import Blueprint, render_template, request, flash, url_for, redirect
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(Email=email).first()
        if user:
            if check_password_hash(user.Password, password):
                flash('logged in succesfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('incorrect password', category='error')
        else:
            flash('User does not exist', category='error')


    return render_template('/login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method =='POST':
        email = request.form.get('Email')
        firstName = request.form.get('firstname')
        lastName = request.form.get('lastname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(Email=email).first()

        if user:
            flash('user already exist.', category='error')
        elif len(email) < 8:
            flash('Email must be greater than 7 character', category='error')
        elif len(firstName) < 2:
            flash('First Name must be at least 2 character long ', category='error')
        elif len(lastName) < 2:
            flash('last Name must be at least 2 character long ', category='error')
        elif password1 != password2:
            flash('Password did not match ', category='error')
        elif len(password1) < 8:
            flash('Length of the password must be at least 8 character long ', category='error')
        else:
            new_user = User(Email=email, Firstname=firstName, Lastname=lastName, Password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully ', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))

    return render_template('sign-up.html')