from django.urls import path
from django.conf.urls import *

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^research/$', views.research, name='research'),
	url(r'^research/neuroimaging/', views.research_neuroimaging, name='research_neuroimaging'),
	url(r'^research/behavioral/', views.research_behavioral, name='research_behavioral'),
    url(r'^publications/', views.publications, name='publications'),
	url(r'^team/$', views.team, name='team'),
    url(r'^join/$', views.join, name='join'),
	url(r'^about_us/', views.about_us, name='about_us'),
	url(r'^equipment/', views.equipment, name='equipment'),
	url(r'^meetings/$', views.meetings, name='meetings'),
	url(r'^news/$', views.news, name='news'),
	url(r'^gallery/', views.gallery, name='gallery'),
	url(r'^team/(?P<item_id>\d+)/$', views.person),
	url(r'^research/(?P<item_id>\d+)/$', views.about),
	url(r'^meetings/seminars/', views.meetings_seminars, name='meetings_seminars'),
	url(r'^meetings/workshops/', views.meetings_workshops, name='meetings_workshops'),
    url(r'^public/$', views.public),
    url(r'^public/media/$', views.public_media),
    url(r'^public/events/$', views.public_events),
    url(r'^robots/$', views.robots), #temporary
]
