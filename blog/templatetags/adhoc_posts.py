from datetime import datetime, timedelta
from django import template
from django.db.models import Q
from oembed.core import replace
from blog.models import Post, Link

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

@register.simple_tag
def most_liked():
    time_ago = datetime.now() - timedelta(days=7)
    posts = Post.objects.filter(timestamp__gte=time_ago).filter(published=True).order_by('-likes')[:5]
    html = '<ul class="unstyled">'

    for p in posts:
        html += '<li><a href="%s">%s</a></li>' % (p.get_absolute_url(), p.title)

    html += '</ul>'

    return html

@register.simple_tag
def blogroll():
    links = Link.objects.filter(contributor=True)

    if links:
        html = '<ul class="unstyled">'

        for l in links:
            html += '<li><a href="%s">%s</a></li>' % (l.url, l.name)

        html += '<li><h4><a href="/friends/" class="more">Friends of AdHoc</a></h4></li>'
        html += '</ul>'
        return html
    else:
        return ''
    
