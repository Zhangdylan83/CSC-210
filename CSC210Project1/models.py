from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(80), nullable=False) 
    products = db.relationship('Product', backref='user')
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

'''
@app.route('/users/<int:uid>')
def user_profile(uid):
    # Since the keys in the JSON are strings, we need to convert the uid to a string for proper matching
    user = users_dict.get(str(uid))
    if not user:
        abort(404)
    return render_template('start.html', user=user, users_dict=users_dict)

@app.errorhandler(404)
def page_not_found(e):
    # Note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True) 
'''