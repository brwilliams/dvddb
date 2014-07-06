from django.contrib import admin
from dvd.models import * #hope this works

admin.site.register(DVD)
admin.site.register(Book)
admin.site.register(Location)
admin.site.register(Shelf)
admin.site.register(SubShelf)
