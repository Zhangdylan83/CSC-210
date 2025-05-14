from flask import Flask, render_template, redirect, url_for, session
from models import db, Product, User
from forms import LoginForm, ProductForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
import unittest
import coverage
import click
from flask.cli import with_appcontext
import os
import sys

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    template_dir = os.path.join(basedir, '..', 'templates')
    static_dir = os.path.join(basedir, '..', 'static')
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'


    # Initialize the database db
    db.init_app(app)

    def get_latest_product():
        return Product.query.order_by(Product.id.desc()).first()


    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        return render_template('home.html')  # You need to create a 'home.html' template


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and check_password_hash(user.password, form.password.data):
                session['user_id'] = user.id
                #return redirect(url_for('user_profile', user_id=user.id)) #we get user_id parameter， but we are trying not to use uer_id in the route
                return redirect(url_for('user_profile'))
            else:
                pass
        return render_template('start.html', form=form)

    @app.route('/logout')
    def logout():
        session.clear()  # Clear all session data
        return redirect(url_for('home'))  # Redirect to the login page

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = generate_password_hash(form.password.data, method="pbkdf2:sha256", salt_length=8)
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        return render_template('register.html', form=form)

    @app.route('/user_profile')
    def user_profile():
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('login'))  # 未登录时重定向到登录页面
        user = db.session.get(User, user_id)
        if user:
            return render_template('profile.html', user=user)
        else:
            return 'Sorry but you have to login first to get access to this page', 404
    

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
