from django.db import models

# Create your models here.
class Tempy(models.Model):
	name = models.CharField(max_length=75)
	is_test = models.BooleanField()

class Media(models.Model):
        shelf = models.ForeignKey(Shelf)
        name = models.CharField(max_length=100)
        UPC = models.DecimalField(max_digits=12, decimal_places=None)
        checked_out = models.BooleanField(default=False)
        who_has = models.CharField(max_length=100, default = 'Brian')
        #something to keep a series together?  looks like ManyToManyField?
        #link to wikipedia?

class DVD(Media):
        ripped_to_server = models.BooleanField(default=False)
        tv_show = models.BooleanField(default=False)
        box_set = models.BooleanField(default=False)
        #link to imdb?

class Book(Media):
        author = models.CharField(max_length=100)
        paperback = models.BooleanField(default=False)
        #link to amazon?

class Location(models.Model): #entertainment, piano, tall bookcase
        name = models.CharField(max_length=100)
        room = models.CharField(max_length=100)
        
class Shelf(models.Model): #first shelf, cabinet, etc
        location = models.ForeignKey(Location)
        name = models.CharField(max_length=100)

class SubShelf(models.Model): #avengers, classics
        #import from shelf again?
        shelf = models.ForeignKey(Shelf)
        name = models.CharField(max_length=100)
        #series?
