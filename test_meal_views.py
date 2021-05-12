"""Meal View tests."""

import os
from unittest import TestCase

from models import db, connect_db

# Set an environmental variable to use a different database for tests 
os.environ['DATABASE_URL'] = "postgresql:///capstone-test"

from app import app

db.create_all()

# Don't have WTForms use CSRF at all, since it's a pain to test
app.config['WTF_CSRF_ENABLED'] = False

class MealViewTestCase(TestCase):
    """Test views for meals."""

    def setUp(self):
        """Stuff to do before every test."""

        # get real python errors instead of flask errors
        app.config['TESTING'] = True

        # don't allow debug toolbar to work during testing
        app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

    def test_meal_categories_page(self):
        with app.test_client() as client:
            res = client.get('/meals')
            self.assertIn(b'Meal Categories', res.data)  
            self.assertIn(b'Beef', res.data) 
            self.assertIn(b'Chicken', res.data) 
            self.assertIn(b'Goat', res.data) 
            self.assertIn(b'View Recipes', res.data) 
            self.assertIn(b'Beef is the culinary name for meat from cattle, particularly skeletal muscle. Humans have been eating beef since prehistoric times.[1] Beef is a source of high-quality protein and essential nutrients.', res.data) 
            self.assertIn(b'Chicken is a type of domesticated fowl, a subspecies of the red junglefowl. It is one of the most common and widespread domestic animals, with a total population of more than 19 billion as of 2011.[1] Humans commonly keep chickens as a source of food (consuming both their meat and eggs) and, more rarely, as pets.', res.data) 
    
    def test_meals_per_category_page(self):
        with app.test_client() as client:
          res = client.get('/meals/1')
          self.assertIn(b'Meal Recipes For: Beef', res.data) 
          self.assertIn(b'Please Note: You need to be signed in to view meal recipes.', res.data) 

# Only public meal page views are tested here. Private routes are tested in user view tests file.
           
