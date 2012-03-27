import urllib, urllib2, json
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandError
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist

from blog.models import Post

class Command(BaseCommand):
    args = '<days>'
    help = 'Gets Facebook Likes for all posts in the last 7 days'

    def handle(self, *args, **options):
        try:
            args[0]
        except IndexError:
            days = 7
        else:
            days = args[0]

        old_date = datetime.now() - timedelta(days=days)
        posts = Post.objects.filter(published=True).filter(timestamp__gte=old_date)
        query = "SELECT url, total_count FROM link_stat WHERE url in ("

        for p in posts:
            url = '%s%s' % (Site.objects.get_current().domain, p.get_absolute_url())
            query += '"%s",' % url

        query = query.rstrip(', ') + ')'
        request_url = "https://graph.facebook.com/fql?" + urllib.urlencode({'q': query, 'format': 'json'})
        self.stdout.write('Querying Facebook\n')
        data = json.loads(urllib2.urlopen(request_url).read())['data']

        for post in data:
            slug = post['url'].split('/')[-2]
            try:
                p = Post.objects.get(slug=slug)
            except ObjectDoesNotExist:
                self.stdout.write("Couldn't find a post with the slug %s\n" % slug)
            else:
                self.stdout.write("Saving %s with %s likes\n" % (slug, post['total_count']))
                p.likes = int(post['total_count'])
                p.save()
