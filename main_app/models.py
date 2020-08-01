from django.db import models

# Create your models here.

#WINE
class Wine(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	price = models.IntegerField()
	year = models.IntegerField()

	# No migration needed for methods
	def __str__(self):
		return self.name