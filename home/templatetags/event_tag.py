from django import template
from home.models import Meeting
from datetime import date

register = template.Library()


@register.simple_tag
def get_coming_event():
    try:
        upcoming = (
            Meeting.objects
            .filter(starts__gte=date.today())
            .order_by('starts')[0]
            )
    except IndexError:
        upcoming = None
    # return Meeting.objects.order_by('-starts')[0]
    return upcoming
