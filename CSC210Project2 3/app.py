from flask import Flask
from models import db
import views
from config import DevelopmentConfig, ProductionConfig, TestingConfig
import os
app = Flask(__name__)

# Determine which configuration to load
env = os.getenv('FLASK_ENV', 'development')
if env == 'production':
    app.config.from_object(ProductionConfig)
elif env == 'testing':
    app.config.from_object(TestingConfig)
else:
    app.config.from_object(DevelopmentConfig)

# Initialize the database with the app
db.init_app(app)

with app.app_context():
    db.create_all()

# Initialize routes
views.setup_routes(app)

if __name__ == '__main__':
    app.run()
