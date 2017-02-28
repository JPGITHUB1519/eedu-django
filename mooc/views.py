from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login

from .models import Programs, Courses
from .forms import UserForm

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

class UserFormView(View):
	form_class = UserForm
	template_name = 'mooc/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form' : form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			# cleaned data (normalized)
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user.set_password(password)
			# save on database
			user.save()
			# login 
			# return User Object if credentials are correct
			user = authenticate(username=username, password=password)
			if user is not None:
				# if the user is active
				if user.is_active:
					return redirect('mooc:index')

		# if not valid data 
		return render(request, self.template_name, {'form' : form})




