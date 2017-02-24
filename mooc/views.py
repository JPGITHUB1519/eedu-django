from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView

from .models import Programs

# Create your views here.
class IndexView(ListView):
	template_name = 'mooc/index.html'
	# objects is the default manager name
	queryset = Programs.objects.all()
	context_object_name = 'programs'