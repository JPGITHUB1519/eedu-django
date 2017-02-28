from django.conf.urls import url

from . import views

app_name = 'users'

urlpatterns = [
	url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
	url(r'^accounts/auth/$', views.AuthView.as_view(), name='auth'),
	url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout'),
	url(r'^accounts/loggedin/$', views.LoggedinView.as_view(), name='loggedin'),
	url(r'^accounts/invalid/$', views.InvalidLoginView.as_view(), name='invalid'),
	url(r'^accounts/register/$', views.RegisterUserView.as_view(), name='register_user'),
	url(r'^accounts/register_success/$', views.RegisterSuccessView.as_view(), name='register_success'),

]