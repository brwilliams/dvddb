from django.db import models

class Media(models.Model):
        shelf = models.ForeignKey(Shelf) #or maybe subshelf?
        name = models.CharField(max_length=100)
        UPC = models.DecimalField(max_digits=12, decimal_places=None)
        checked_out = models.BooleanField(default=False)
        who_has = models.CharField(max_length=100, default = 'Brian')
        copies = models.IntegerField(default=1)
        #year?  looks complicated to do "right"
        #genre?
        #something to keep a series together?  looks like ManyToManyField?
        #link to wikipedia?
        def __unicode__(self):
		return self.name

class DVD(Media):
        ripped_to_server = models.BooleanField(default=False)
        tv_show = models.BooleanField(default=False)
        box_set = models.BooleanField(default=False)
        director = models.CharField(max_length=100)
        #actors = many to many?
        #link to imdb?

class Book(Media):
        author = models.CharField(max_length=100)
        paperback = models.BooleanField(default=False)
        own_ebook = models.BooleanField(default=False)
        #link to amazon?

class CD(Media): #don't think I'll do this, but just in case

class Location(models.Model): #entertainment, piano, tall bookcase
        name = models.CharField(max_length=100)
        room = models.CharField(max_length=100)
        def __unicode__(self):
		return self.name
        
class Shelf(models.Model): #first shelf, cabinet, etc
        location = models.ForeignKey(Location)
        name = models.CharField(max_length=100)
        def __unicode__(self):
		return self.name

class SubShelf(models.Model): #avengers, classics
        #import from shelf again?
        shelf = models.ForeignKey(Shelf)
        name = models.CharField(max_length=100)
        #series?
        def __unicode__(self):
		return self.name
