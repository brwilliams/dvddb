from django.db import models

# Create your models here.
class Tempy(models.Model):
	name = models.CharField(max_length=75)
	is_test = models.BooleanField()
