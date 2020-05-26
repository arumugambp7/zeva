from django.db import models
from cloudinary.models import CloudinaryField

import cloudinary

# Create your models here.

class Menu(models.Model):
     category = models.CharField(max_length=3,primary_key=True)
     image = CloudinaryField('image')
     title = models.CharField(max_length=25)
     class meta:
          db_table = 'Menu'
     def __str__(self):
          return self.title



class Collection(models.Model):
     name = models.CharField(max_length=6)
     image = CloudinaryField('image')
     menu = models.ManyToManyField(Menu)
     class meta:
          db_table = 'Collection'
     def __str__(self):
          return self.name


class Client(models.Model):
     name = models.CharField(max_length=25,blank=True)
     image = CloudinaryField('image')
     location = models.CharField(max_length=25,blank=True)
     contact = models.CharField(blank=True,max_length=10)
     email = models.EmailField(blank=True)
     menu = models.ManyToManyField(Menu,blank=True)
     class meta:
          db_table = 'Client'
     def __str__(self):
          return self.name

class Subscriber(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(blank=True)
    def __str__(self):
        return self.name



