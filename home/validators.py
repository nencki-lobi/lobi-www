from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def validate_orcid(value):
    """Based on wikidata.org and corroborated by
    https://support.orcid.org/hc/en-us/articles/360006897674
    """
    orc = re.compile(r'0000-000(1-[5-9]|2-[0-9]|3-[0-4])\d{3}-\d{3}[\dX]')
    if not re.match(orc, value):
        raise ValidationError(
            _('%(value)s is not a valid ORCID number.'),
            params={'value': value},
        )


def validate_github(value):
    """Best we can do is to check if it's not a full address"""
    if 'github.com/' in value:
        raise ValidationError(
            _('This field should not contain the full address'),
            params={},
        )


def validate_scholar(value):
    """Based on wikidata.org"""
    if not re.match(r'[-_0-9A-Za-z]{12}', value):
        raise ValidationError(
            _('%(value)s is not a valid scholar ID.'),
            params={'value': value},
        )
