from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        email_checker = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_checker.match(postData['email']):
            errors['email'] = 'Must be a valid email'
        if postData['password'] != postData['password_conf']:
            errors['pass'] = 'Nope, your passwords did not match. Try again.'
        return errors
    def login_validator(self, postData):
        errors = {}
        email_checker = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_checker.match(postData['email']):
            errors['email'] = 'Must be a valid email'
        return errors

class User(models.Model):
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # description = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Wall_Message(models.Model):
    message = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='user_messages', on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(User, related_name='liked_posts')

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    wall_message = models.ForeignKey(Wall_Message, related_name="post_comments", on_delete=models.CASCADE)

class Grocery_List(models.Model):
    item = models.CharField(max_length=50)
    creator = models.ForeignKey(User, related_name='user_lists', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
#--------------- Added Classes ----------------------
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)
    creator = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)

class Meal(models.Model):
    scheduled_for = models.DateField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)