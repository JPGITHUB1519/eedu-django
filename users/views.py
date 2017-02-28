from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


# Create your views here.
class LoginView(View):
	def get(self, request):
		return render(request, "users/login.html")

class AuthView(View):
	def get(self, request):
		return HttpResponse("Hello!")
	def post(self, request):
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('users:loggedin'))
			#return HttpResponseRedirect('/accounts/loggedin/')
		else:
			return HttpResponseRedirect(reverse('users:invalid'))
			#return HttpResponseRedirect('/accounts/invalid/')

class LoggedinView(View):
	def get(self, request):
		return render(request, 'users/loggedin.html',
								{'fullname' : request.user.username })

class InvalidLoginView(View):
	def get(self, request):
		return render(request, 'users/invalid_login.html')

class LogoutView(View):
	def get(self, request):
		#	logout
		logout(request)
		return render(request, 'users/logout.html')

class RegisterUserView(View):
	def get(self, request):
		form = UserCreationForm(None)
		return render(request, 'users/register.html', {'form': form})

	def post(self, request):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			# save user
			form.save()
			return HttpResponseRedirect(reverse("users:register_user"))
		return render(request, 'users/register.html', {'form': form})

class RegisterSuccessView(View):
	def get(self, request):
		return render(request,'users/register_success.html')

