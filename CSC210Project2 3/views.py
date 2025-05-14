from flask import render_template, redirect, url_for, session, request, current_app as app

# Import database setup, models, and forms
from models import db, User, GameScore
from forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash

def setup_routes(app):
    
    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and check_password_hash(user.password, form.password.data):
                session['user_id'] = user.id
                return redirect(url_for('scores'))
            else:
                return render_template('start.html', form=form, error="Invalid credentials.")
        return render_template('start.html', form=form)

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

    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login')) 

    @app.route('/game')
    def game():
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return render_template('game.html')

    @app.route('/scores')
    def scores():
        if 'user_id' not in session:
            return redirect(url_for('login'))
        all_scores = GameScore.query.all()
        return render_template('scores.html', scores=all_scores)

    @app.route('/delete_score/<int:score_id>', methods=['POST'])
    def delete_score(score_id):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        score = GameScore.query.get(score_id)
        if score and score.user_id == session['user_id']:
            db.session.delete(score)
            db.session.commit()
            return redirect(url_for('scores'))
        return 'Score not found', 404

    @app.route('/record_score', methods=['POST'])
    def record_score():
        if 'user_id' not in session:
            return redirect(url_for('login'))

        data = request.get_json()
        new_score = GameScore(
            user_id=session['user_id'],
            score=data['score'],
            trials=data['trials']
        )
        db.session.add(new_score)
        db.session.commit()

        return {'message': 'Score recorded successfully'}
