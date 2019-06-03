from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	position = models.CharField("Position",max_length=200,blank=True)
	degree = models.CharField("Academic degree",max_length=20,blank=True)
	affiliated = models.BooleanField("Check for affiliated members",default=False)
	spoiler = models.ImageField("Email spoiler graphic",upload_to="users",blank=True)
	priority = models.IntegerField("Priority (the more the higher at page)",blank=False,default=-1)
	about = models.TextField("About (html allowed)",max_length=2000,blank=True)
	phone = models.CharField("Phone number",max_length=20,blank=True)
	research = models.TextField("Research interests (html allowed)",max_length=2000,blank=True)
	publications = models.TextField("Selected publications (html allowed)",max_length=12000,blank=True)
	funding = models.TextField("Funding (html allowed)",max_length=2000,blank=True)
	orcid = models.CharField("Orcid ID", max_length=32, blank=True, help_text="0000-0000-0000-0000")
	github = models.CharField("GitHub username", max_length=32, blank=True)
	scholar = models.CharField("Google scholar ID", max_length=32, blank=True, help_text="Enter just the ID. This is part of an url, e.g. https://scholar.google.pl/citations?user=<strong>qTDPssQAAAAJ</strong>&hl=pl")
	image = models.ImageField("Face",upload_to="users",blank=True)
	my_dish = models.CharField("I can cook...",max_length=200,blank=True)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Alumni(models.Model):
	name = models.CharField("Full name",max_length=200)
	more = models.CharField("Additional info",max_length=200)

	class Meta:
		verbose_name_plural = "Alumni"

class Research(models.Model):
	NEURO = 'NRI'
	BEHAV = 'BHV'
	RESEARCH_CHOICES = (
		(NEURO, 'Neuroimaging'),
		(BEHAV, 'Behavioral'),
	)
	title = models.CharField("Title",max_length=200)
	investigator = models.CharField("Principal Investigator",max_length=200)
	institution = models.CharField("Institution name (lab)",max_length=200)
	priority = models.IntegerField("Priority (the more the higher at page)",blank=False,default=0)
	about = models.TextField("More information (html allowed)",max_length=5000,blank=True)
	bold = models.BooleanField()
	image = models.ImageField("Graphic",upload_to="research",blank=True)
	about_image = models.TextField("Image caption",max_length=500,blank=True)
	link = models.CharField("External link (start with http://...)",max_length=500,blank=True)
	web = models.CharField("Frame content (start with http://...)",max_length=500,blank=True)
	#inter_exter = models.BooleanField("Internal LOBI project")
	research_type = models.CharField(max_length=3,choices=RESEARCH_CHOICES,default=NEURO)
	
	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural = "Research"

class Publication(models.Model):
	title = models.CharField("Title",max_length=200)
	authors = models.CharField("Authors (html allowed)",max_length=400)
	published = models.DateField("Publication date (leave empty if not published)",null=True,blank=True)
	about = models.TextField("More information (html allowed)",max_length=2000,blank=True)
	bold = models.BooleanField()
	image = models.ImageField("Graphic",upload_to="research",blank=True)
	link = models.CharField("External link (start with http://...)",max_length=500,blank=True)
	
	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural = "Publications"

class Course(models.Model):
	MRUSER = 'MRUC'
	LABMEETING = 'LABM'
	OPENING = 'LOPN'
	COURSE_CHOICES = (
		(MRUSER, 'MR User Club'),
		(LABMEETING, 'Lab Meeting'),
	)
	title = models.CharField("Course title",max_length=200)
	starts = models.DateTimeField("Starting date")
	ends = models.DateTimeField("Ending date",null=True,blank=True)
	old = models.BooleanField("Show date",default=True)
	people = models.CharField("Speaker and/or organizers",max_length=200)
	about = models.TextField("More information (place etc., html allowed)",max_length=5000)
	bold = models.BooleanField()
	image = models.ImageField("Graphic",upload_to="research",blank=True)
	link = models.CharField("External link (start with http://...)",max_length=500,blank=True)
	event_type = models.CharField(max_length=4,choices=COURSE_CHOICES,default=LABMEETING)

	@property
	def upcoming(self):
		if datetime.date.today() < self.starts.date():
			return True
		return False
	
	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural = "Courses"

class Photo(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField("foto",upload_to="photos")
	
	def __unicode__(self):
		return self.title

class News(models.Model):
	date = models.DateTimeField("Date",auto_now=True)
	title = models.CharField("Title",max_length=200)
	content = models.TextField("News content (html allowed)",max_length=2000)
	image = models.ImageField("News image",upload_to="news",blank=True)
	
	def __unicode__(self):
		return self.title
		
	class Meta:
		verbose_name_plural = "News"
