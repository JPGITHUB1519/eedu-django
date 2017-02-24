from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Programs(models.Model):
	name = models.CharField(max_length=50)
	slogan = models.TextField(max_length=5000)
	description = models.TextField(max_length=5000)
	cost = models.DecimalField(max_digits=6, decimal_places=2)
	has_plus = models.BooleanField(default=True)
	is_active = models.BooleanField(default=True)
	timeline = models.IntegerField(default=0)
	released_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name