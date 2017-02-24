from django.contrib import admin

from .models import Programs, Courses
# Register your models here.
admin.site.register(Courses)
admin.site.register(Programs)