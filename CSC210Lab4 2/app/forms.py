from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, EmailField
from wtforms.validators import DataRequired
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    #email = EmailField('Email', validators=[DataRequired(), Email()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Add Product')

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