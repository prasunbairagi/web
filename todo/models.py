from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=200)
    mobile=models.CharField(max_length=15)
    query=models.CharField(max_length=255)