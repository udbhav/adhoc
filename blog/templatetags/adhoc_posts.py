from django import template
from django.db.models import Q
from oembed.core import replace

register = template.Library()

@register.filter
def return_embeds(post, position):
    embeds = post.embeds.filter(position = str(position))
    text = ''
    for e in embeds:
        if e.music_embed:
            text += '\n' + e.music_embed.get_html()
        else:
            text += e.body + '\n'

    text = replace(text)

    return text

@register.filter
def read_more(post):
    bottom_embeds = post.embeds.filter(Q(position='3') | Q(position='4'))
    if post.read_more or bottom_embeds:
        return True
    else:
        return False
