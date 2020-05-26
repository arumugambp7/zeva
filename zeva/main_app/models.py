from django.db import models
from cloudinary.models import CloudinaryField

import cloudinary

# Create your models here.

class Category(models.Model):
     category = models.CharField(max_length=3,primary_key=True)
     image = CloudinaryField('image')
     title = models.CharField(max_length=25)
     class meta:
          db_table = 'Category'
     def __str__(self):
          return self.title



class Tutus(models.Model):
     name = models.CharField(max_length=6)
     image = CloudinaryField('image')
     menu = models.ManyToManyField(Category)
     class meta:
          db_table = 'Tutus'
     def __str__(self):
          return self.name


class Customer(models.Model):
     name = models.CharField(max_length=25,blank=True)
     image = CloudinaryField('image')
     location = models.CharField(max_length=25,blank=True)
     contact = models.CharField(blank=True,max_length=10)
     email = models.EmailField(blank=True)
     menu = models.ManyToManyField(Category, blank=True)
     class meta:
          db_table = 'Customer'
     def __str__(self):
          return self.name

class Follower(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    # message = models.TextField(blank=True)
    def __str__(self):
        return self.name



