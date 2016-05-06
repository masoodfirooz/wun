from django.conf.urls import patterns, include, url

from showevents import views

urlpatterns = [
	url(r'^$', views.home, name='showevents'),
]