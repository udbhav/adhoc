from django import template
from datetime import datetime

from src.advertising.models import *

register = template.Library()

@register.simple_tag
def place_ad(ad_position):
    try:
        ad = Advertisement.objects.filter(position=ad_position).filter(start_date__lte=datetime.now()).filter(end_date__gte=datetime.now())[0]
    except IndexError:
        ad = None

    html = ''
    if ad:
        if ad.code:
            html = ad.code
        else:
            html = '<a href="%s"><img src="%s" alt="%s" /></a>' % (ad.url, ad.image.url, ad.title)

        if ad_position == '2' or ad_position == '3':
            html = '<li>' + html + '</li>'

    return html
