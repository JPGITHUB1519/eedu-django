from django.conf.urls import url

from . import views

app_name = 'mooc'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name="index"),
	url(r'^register/$', views.UserFormView.as_view(), name='register'),
	url(r'^program/(?P<pk>[0-9]+)/$', views.ProgramView.as_view(), name='program'),
	url(r'^courses/$', views.CoursesView.as_view(), name='courses'),
	url(r'^courses/(?P<pk>[0-9]+)/$', views.CourseView.as_view(), name='course'),
]