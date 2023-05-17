import unittest
from flask import Flask, template_rendered
from flask_mysqldb import MySQL
from flask_testing import TestCase
from app import app

# Import your Flask app here

class AppTestCase(TestCase):
def create_app(self):
app = Flask(__name__)
app.config['TESTING'] = True
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskcrud'
app.secret_key = "mysecretkey"
return app

def setUp(self):
# Set up any necessary database fixtures or test data
pass

def tearDown(self):
# Clean up after each test
pass

def test_index(self):
response = self.client.get('/')
self.assert200(response)
# Add assertions to verify the response data

def test_add_contact(self):
response = self.client.post('/add_contact', data={'fullname': 'John', 'phone': '123456789', 'email': 'john@example.com'})
self.assertRedirects(response, '/')

if __name__ == '__main__':
unittest.main()
