from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('/login.html')

@auth.route('/logout')
def logout():
    return "<h1>logout</h1>"

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method =='POST':
        email = request.form.get('Email')
        firstname = request.form.get('firstname')
        lastName = request.form.get('lastname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 8:
            flash('Email must be greater than 7 character', category='error')
        elif len(firstname) < 2:
            flash('First Name must be at least 2 character long ', category='error')
        elif len(lastName) < 2:
            flash('last Name must be at least 2 character long ', category='error')
        elif password1 != password2:
            flash('Password did not match ', category='error')
        elif len(password1) < 8:
            flash('Length of the password must be at least 8 character long ', category='error')
        else:
            flash('User added successfully ', category='success')

    return render_template('sign-up.html')