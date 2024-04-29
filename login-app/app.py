from flask import Flask;
from flask import render_template;
from flask import url_for;
from flask_sqlalchemy import SQLAlchemy;
from flask_login import UserMixin;
from sqlalchemy.sql import func;

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template("/login.html")

@app.route("/register")
def register():
    return render_template("/register.html")

if __name__ == '__main__':
    app.run(debug=True)