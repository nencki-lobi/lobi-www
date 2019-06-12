from django import template
from home.models import Photo

register = template.Library()

#@register.assignment_tag
#def get_random_photo():
#    return Photo.objects.order_by('?')[0]

@register.inclusion_tag('home/photo_sample.html')
def get_random_photos():
    photos = Photo.objects.order_by('?')[:2]
    return {'photos': photos}
