#from django.http import HttpResponse
from django.shortcuts import render_to_response
#from django.template import Context, loader, RequestContext
from home.models import News, Alumni, Research, Publication, Course, Photo
from django.contrib.auth.models import User
from datetime import date

def index(request):
    news = News.objects.all().order_by('-date')[:4]
    return render_to_response('home/index.html', {'news' : news})

def team(request):
	team = User.objects.filter(profile__affiliated=False).order_by('-profile__priority')
	alumni = Alumni.objects.all()
	affiliated = User.objects.filter(profile__affiliated=True).order_by('-profile__priority')
	return render_to_response('home/team.html', {'team' : team, 'alumni' : alumni, 'affiliated' : affiliated })

def about_us(request):
	return render_to_response('home/about_us.html')

def research(request):
	research = Research.objects.all().order_by('-priority')
	return render_to_response('home/research.html', {'research' : research})

def research_neuroimaging(request):
	research = Research.objects.filter(research_type='NRI').order_by('-priority')
	return render_to_response('home/research_neuro.html', {'research' : research})

def research_behavioral(request):
	research = Research.objects.filter(research_type='BHV').order_by('-priority')
	return render_to_response('home/research_behav.html', {'research' : research})

def publications(request):
	preparation = Publication.objects.exclude(published__isnull=False)
	publications = Publication.objects.exclude(published__isnull=True).order_by('-published')
	return render_to_response('home/publications.html', {'publications' : publications, 'preparation' : preparation})

def equipment(request):
    return render_to_response('home/equipment.html')

def courses(request):
	future_courses = Course.objects.filter(starts__gt=date.today()).order_by('starts')
	past_courses = Course.objects.filter(starts__lt=date.today()).order_by('-starts')
	return render_to_response('home/courses.html', {'future_courses' : future_courses, 'past_courses' : past_courses})

def gallery(request):
	photos = Photo.objects.all()
	return render_to_response('home/gallery.html', {'photos' : photos })

def person(request, item_id):
	user = User.objects.get(id=item_id)
	has_social = any((user.profile.orcid, user.profile.scholar, user.profile.github))
	return render_to_response('home/person.html', {'user':  user, 'show_social': has_social})

def about(request, item_id):
	item = Research.objects.get(id=item_id)
	return render_to_response('home/about.html', {'item' :  item})

def courses_mruser(request):
	future_courses = Course.objects.filter(starts__gt=date.today(),event_type='MRUC').order_by('starts')
	past_courses = Course.objects.filter(starts__lt=date.today(),event_type='MRUC').order_by('-starts')
	return render_to_response('home/courses.html', {'future_courses' : future_courses, 'past_courses' : past_courses})

def courses_labmeeting(request):
	future_courses = Course.objects.filter(starts__gt=date.today(),event_type='LABM').order_by('starts')
	past_courses = Course.objects.filter(starts__lt=date.today(),event_type='LABM').order_by('-starts')
	return render_to_response('home/courses.html', {'future_courses' : future_courses, 'past_courses' : past_courses})

def courses_labopening(request):
    return render_to_response('home/labopening.html')

def news(request):
	news = News.objects.all().order_by('-date')
	return render_to_response('home/news.html', {'news' : news})

def public(request):
	#news = News.objects.all().order_by('-date')
	return render_to_response('home/robots.html')

def robots(request):
	#news = News.objects.all().order_by('-date')
	return render_to_response('home/robots.html')
