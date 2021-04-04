from django.db import models
import re, datetime

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 5 or postData['title'] == None:
            errors["title"] = "Course title should be at least 5 characters."
        # print(postData)
        if len(postData['descr']) < 15:
            errors["descr"] = "Description should be at least 15 characters."              
        return errors

class Course(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

class Descr(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True)
    descr = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()