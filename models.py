from django.db import models

class Media(models.Model):
        shelf = models.ForeignKey(Shelf) #or maybe subshelf?
        name = models.CharField(max_length=100)
        UPC = models.DecimalField(max_digits=12, decimal_places=None)
        checked_out = models.BooleanField(default=False)
        who_has = models.CharField(max_length=100, default = 'Brian')
        copies = models.PositiveSmallIntegerField(default = 1)
        condition = models.TextField()
        wiki = models.URLField()
        amazon = models.URLField()
        genre_choices = ( #https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.Field.choices
                ('SF', 'Sci-fi'),
                ('FAN', 'Fantasy'),
                ('COM', 'Comedy'),
                ('NF', 'Non-fiction'),
                ('SH', 'Superhero'),
                ('GA', 'Generic Action'),
                ('SPR', 'Sports')
                ('O', 'Other'),
        )
        genre = models.CharField(max_length=3, choices = genre_choices, default = 'O')
        #year?  looks complicated to do "right"
        #something to keep a series together?  looks like ManyToManyField?        def __unicode__(self):
        def __unicode__(self):
                return self.name

class DVD(Media):
        ripped_to_server = models.BooleanField(default=False)
        tv_show = models.BooleanField(default=False)
        box_set = models.BooleanField(default=False)
        widescreen = models.BooleanField(default=True)
        blu_ray = models.BooleanField(default=False)
        number_of_discs = models.PositiveSmallIntegerField(default = 1)
        runtime_in_minutes = models.PositiveSmallIntegerField() #is there a better way to do this
        director = models.CharField(max_length=100) #maybe make a director class
        #actors = many to many?
        imdb = models.URLField()

class Book(Media):
        author = models.CharField(max_length=100)
        paperback = models.BooleanField(default=False)
        own_ebook = models.BooleanField(default=False)
        pages = models.PositiveSmallIntegerField()
        #some sort of size choice?  like trade paperback, mass media, etc
        #something like "if textbook, what course?"

class CD(Media): #don't think I'll do this, but just in case
        artist = models.CharField(max_length=100)
        number_of_tracks = models.PositiveSmallIntegerField()

class VideoGames(Media): #same
        console = models.ForeignKey(Console)

class Console(models.Model): #just in case
        name = models.CharField(max_length=100)
        #place in house?

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
