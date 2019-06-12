from django import template
from home.models import Meeting
from datetime import date

register = template.Library()

@register.simple_tag
def get_coming_event():
    return Meeting.objects.order_by('-starts')[0]

#@register.inclusion_tag('home/photo_sample.html')
#def get_random_photos():
#    photos = Photo.objects.order_by('-date)[:2]
#    return {'photos': photos}
