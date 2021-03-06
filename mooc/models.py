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
	skill_level = models.CharField(max_length=50, null=True, choices=[("beginner", "beginner"), ("intermediate", "intermediate"), ("advanced", "advanced")])

	def __str__(self):
		return self.name

class Courses(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	slogan = models.TextField()
	cost = models.DecimalField(max_digits=6, decimal_places=2)
	timeline = models.IntegerField(default=0)
	released_date = models.DateField(auto_now_add=True)
	is_active = models.BooleanField(default=True)
	# many to many relations with Programs
	programs = models.ManyToManyField(Programs)
	skill_level = models.CharField(max_length=50, null=True, choices=[("beginner", "beginner"), ("intermediate", "intermediate"), ("advanced", "advanced")])

	def __str__(self):
		return self.name
