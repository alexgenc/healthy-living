# HEALTHY LIVING - CAPSTONE PROJECT 1 - ALEX GENC

## ABOUT THE PROJECT
The intention of this project is to create a full-stack web application using all the technologies learned up to this point (~40%) in Springboard's Software Engineering Career Track course.

This project, called Healthy Living, uses the following technologies:
  - HTML
  - CSS
  - JavaScript
  - Ajax
  - Python
  - Flask
  - Jinja
  - WTForms
  - PostgreSQL
  - SQLAlchemy

## Routes
  - / - Home Route - Lists latest healthy eating and exercise news
  
  ### User Routes
  - /register - User registration route.
  - /login - User login route.
  - /logout - User logout route.
  - /users/<username> - User dashboard route.
  - /users/<username>/settings - Change user settings route.
  - /users/<username>/change-password - Change user password route.
  - /users/<username>/delete - User account deletion route.
  - /users/<username>/meals/add - Adding meals to user's meals route.
  - /users/<username>/meals/remove - Removing meals from user's meals route.
  - /users/<username>/exercises/add - Adding exercises to user's exercises route.
  - /users/<username>/exercises/remove - Removing exercises from user's exercises route.
  - /exercise-comments/<comment_id>/delete - Deleting exercise comment route.
  - /meal-comments/<comment_id>/delete - Deleting meal comment route.

  ### Exercise Routes
  - /exercises - All exercise categories route.
  - /exercises/<category_id> - Exercises for a specific exercise category route. 
  - /exercises/<category_id>/<exercise_id> - Exercise details route.
  - /exercises/<category_id>/<exercise_id>/comment - Exercise comment route.
  
  ### Meal Routes
  - /meals - Allow users to view meal categories or directly search for a meal.
  - /meal-categories - All meal categories route.
  - /meals/search - Meal search route.
  - /meals/<category_id> - Meals for a specific meal category route. 
  - /meals/<category_id>/<meal_id> - Meal details route.
  - /meals/<category_id>/<meal_id>/comment - Meal comment route.
 
## User Flows

Users who are not logged in will be able to view latest news on the homepage, exercise and meal categories, as well as the list of exercises and meals for each category. However, they will not be able to view specific meal or exercise pages.

Logged in users will be able to view specific meal and exercise pages, post comments on meals and exercises, add meals and exercises to their favorites. Logged in users also have access to their user dashboard, which they can use to update their account information and change password. User dashboard also displays a user's favorite meals, exercises, as well as their comments on different meals and exercises.

## Password Protection

All passwords are salted and encrypted using BCrypt, using the wrapper flask-bcrypt and the hash is saved on the database. This adds a layer of security to the password and make it harder to be cracked.

## API
**Exercises API:** https://wger.de/en/software/api  
**Meals API:** https://www.themealdb.com/api.php  
**News API:** https://open-platform.theguardian.com/ 

## Database Schema Design
![Database-Schema-Design.jpg](https://i.postimg.cc/VvmntCtK/Database-Schema-Design.jpg)

**Meal information is directly fetched from the API and therefore, not stored in the database.**

## Testing

There are a total of 6 test files. 3 of them are for model tests, and the remaning 3 are for view tests.
  - test_exercise_models.py - Test exercise instances, user exercises, and user exercise comments.
  - test_meal_models.py - Test meal instances, user meals, and user meal comments.
  - test_user_model.py : Test user registration, user login, invalid registration and login cases, changing password, and more.
  - test_exercise_views.py - Test if exercise related routes display as intended.
  - test_meal_views.py - Test if meal related routes display as intended.
  - test_user_views.py - Test if user related routes display as intended.
