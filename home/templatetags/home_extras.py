from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()

@register.filter
@stringfilter
def dropptag(value):
    """Removes opening / closing tags from beginning and end.
    Use before safe."""

    new_value = re.sub(r'^<p>', '', value)  # opening
    new_value = re.sub(r'</p>\s*$', '', new_value)  # closing + trailing whtsp
    return new_value
