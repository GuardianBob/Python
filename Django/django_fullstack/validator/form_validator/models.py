from django.db import models
import re  # Regex module

#==========================Lesson Examples================================
# Inside your app's models.py file
# imports
class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BlogManager()    # add this line!
"""
models come with a hidden property:
    objects = models.Manager()
we are going to override this!
"""

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 5:
            errors["name"] = "Blog name should be at least 5 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        # check for email errors
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
        return errors