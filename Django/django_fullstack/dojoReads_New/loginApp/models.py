from django.db import models
import re, datetime
import bcrypt

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

