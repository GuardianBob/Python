from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# =============Provided from Solution===============
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"