# tests/test_auth.py
import unittest
from flask_testing import TestCase
from app.app import create_app, db, User

class BaseTestCase(TestCase):
    """A base test case for flask-tracking."""

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class FlaskTestCase(BaseTestCase):
    
    def test_registration(self):
        """Ensure the registration behaves correctly."""
        response = self.client.post('/register', data=dict(
            username='testuser',
            email='test@example.com',
            password='password123',
            confirm_password='password123'
        ), follow_redirects=True)
        self.assertIn(b'Login', response.data)

    def test_login_logout(self):
        """Test login and logout using helper functions."""
        self.client.post('/register', data=dict(
            username='testlogin',
            email='testlogin@example.com',
            password='password123',
            confirm_password='password123'
        ), follow_redirects=True)
        response = self.client.post('/login', data=dict(
            username='testlogin',
            password='password123'
        ), follow_redirects=True)
        self.assertIn(b'Profile', response.data)
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Home', response.data)

    def test_access_control(self):
        """Ensure that unauthenticated users are redirected to the login page."""
        response = self.client.get('/user_profile', follow_redirects=True)
        self.assertIn(b'Login', response.data)


    def test_user_profile_access(self):
        """Ensure that authenticated users can access the user profile page."""
        # Create a test user
        self.client.post('/register', data=dict(
            username='testuser',
            email='test@example.com',
            password='password123',
            confirm_password='password123'
        ), follow_redirects=True)

        # Log in as the test user
        self.client.post('/login', data=dict(
            username='testuser',
            password='password123'
        ), follow_redirects=True)

        # Test access to user profile page after logging in
        response = self.client.get('/user_profile', follow_redirects=True)
        self.assertIn(b'Profile', response.data)

if __name__ == '__main__':
    unittest.main()
