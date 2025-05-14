from flask import Flask, render_template, redirect, url_for, session
from models import db, Product, User
from forms import LoginForm, ProductForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'


# Initialize the database db
db.init_app(app)

def get_latest_product():
    return Product.query.order_by(Product.id.desc()).first()


with app.app_context():
    db.create_all()

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
    user = User.query.get(user_id)
    if user:
        return render_template('profile.html', user=user)
    else:
        return 'User not found', 404
    
@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)
    
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        user_id = session.get('user_id')
        new_product = Product(name=form.name.data, description=form.description.data, price=form.price.data, user_id=user_id)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('product_detail', product_id=new_product.id))
    return render_template('add_product.html', form=form)

@app.route('/delete_product/<int:product_id>')
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    # 检查是否当前登录用户添加的产品
    if product.user_id == session.get('user_id'):
        db.session.delete(product)
        db.session.commit()
        return redirect(url_for('products'))
    else:
        # 如果不是，返回错误或拒绝访问
        return 'Error: You are not authorized to delete this product', 403
    
@app.route('/products')
def products():
    all_products = Product.query.all()
    user_id = int(session.get('user_id', 0))
    return render_template('products.html', products=all_products, user_id=user_id)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)