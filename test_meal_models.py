"""Meal model tests."""

import os
from unittest import TestCase
from sqlalchemy import exc

from models import db, User, MealCategory, UserMeal, MealComment

# Set an environmental variable to use a different database for tests 
os.environ['DATABASE_URL'] = "postgresql:///capstone-test"

from app import app

db.create_all()

class MealModelTestCase(TestCase):
    """Test meal models."""

    def setUp(self):
        """Create test client, add sample data."""
        
        db.drop_all()
        db.create_all()

        # Create test meal categories
        c1 = MealCategory(name="Beef", description="Beef meals", image_url="img1")
        c1.id = 10
        c2 = MealCategory(name="Chicken", description="Chicken meals", image_url="img2")
        c2.id = 11

        db.session.add_all([c1,c2])
        
        db.session.commit()

        self.client = app.test_client()

    def tearDown(self):
        """Tear down after tests are completed"""
        res = super().tearDown()
        db.session.rollback()
        return res

    def test_meal_category(self):
        """Test basic meal category model."""

        # Create test meal categories
        c3 = MealCategory(name="Vegan", description="Vegan meals", image_url="img3")
        c3.id = 12
        c4 = MealCategory(name="Goat", description="Goat meals", image_url="img4")
        c4.id = 13

        db.session.add_all([c3,c4])
        
        db.session.commit()

        mc = MealCategory.query.all()

        self.assertEqual(len(mc), 4) # 2 categories were created in setUp() and we created 2 more here.
        self.assertEqual(mc[0].id, 10)
        self.assertEqual(mc[0].name, "Beef")
        self.assertEqual(mc[1].id, 11)
        self.assertEqual(mc[1].name, "Chicken")
        self.assertEqual(mc[2].id, c3.id)
        self.assertEqual(mc[2].name, "Vegan")
        self.assertEqual(mc[3].id, c4.id)
        self.assertEqual(mc[3].name, "Goat")

    def test_user_meal_model(self):
        """Test adding meals to a user's meals functionality."""

        # The meal data is fetched from an API but here we'll mimic meal data to test user_meal model.
        # Create test meals
        
        #meal1
        m1_id = 555
        m1_name = "Beef Meal"

        #meal2
        m2_id = 666
        m2_name = "Chicken Meal"
        
        # Create test user
        u = User.register("testing1", "password", "testing@test.com", "John", "Doe", None)
        u.id = 777

        db.session.commit()

        um1 = UserMeal(user_id=u.id, meal_id=m1_id, meal_name=m1_name, meal_category=10)
        um2 = UserMeal(user_id=u.id, meal_id=m2_id, meal_name=m2_name, meal_category=11)

        db.session.add_all([um1, um2])

        db.session.commit()

        m = UserMeal.query.filter_by(user_id=u.id)

        self.assertEqual(m.count(), 2)
        self.assertEqual(m[0].meal_id, m1_id)
        self.assertEqual(m[0].meal_name, m1_name)
        self.assertEqual(m[0].meal_category, 10)
        self.assertEqual(m[1].meal_id, m2_id)
        self.assertEqual(m[1].meal_name, m2_name)
        self.assertEqual(m[1].meal_category, 11)

        
    def test_meal_comment_model(self):
        """Test user commentting functionality on a meal."""

        # The meal data is fetched from an API but here we'll mimic meal data to test user_meal model.
        # Create test meals
        
        #meal1
        m1_id = 555
        m1_name = "Beef Meal"

        #meal2
        m2_id = 666
        m2_name = "Chicken Meal"
        
        # Create test user
        u = User.register("testing1", "password", "testing@test.com", "John", "Doe", None)
        u.id = 777

        db.session.commit()

        uc1 = MealComment(content="Test1", user_id=u.id, meal_id=m1_id, meal_name=m1_name, meal_category=10)
        uc2 = MealComment(content="Test2", user_id=u.id, meal_id=m2_id, meal_name=m2_name, meal_category=11)
    
        db.session.add_all([uc1, uc2])

        db.session.commit()

        ucs = MealComment.query.filter_by(user_id=u.id)

        self.assertEqual(ucs.count(), 2)
        self.assertEqual(ucs[0].meal_id, m1_id)
        self.assertEqual(ucs[0].meal_name, m1_name)
        self.assertEqual(ucs[0].meal_category, 10)
        self.assertEqual(ucs[0].user_id, u.id)
        self.assertEqual(ucs[1].meal_id, m2_id)
        self.assertEqual(ucs[1].meal_name, m2_name)
        self.assertEqual(ucs[1].meal_category, 11)
        self.assertEqual(ucs[1].user_id, u.id)