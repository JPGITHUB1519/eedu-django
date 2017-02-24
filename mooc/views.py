from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .models import Programs, Courses

# Create your views here.
class IndexView(ListView):
	template_name = 'mooc/index.html'
	# objects is the default manager name
	queryset = Programs.objects.all()
	context_object_name = 'programs'

class ProgramView(DetailView):
	""" Show one specific Program """
	model = Programs
	template_name = 'mooc/program.html'
	context_object_name = "program"

class CoursesView(ListView):
	""" Show all Available Courses """
	template_name = 'mooc/courses.html'
	queryset = Courses.objects.all()
	context_object_name = 'courses'

class CourseView(DetailView):
	""" Show one Course and his details """
	model = Courses
	template_name = 'mooc/course.html'
	context_object_name = 'course'


