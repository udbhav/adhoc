from haystack.indexes import *
from haystack import site
from blog.models import Post


class PostIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

site.register(Post, PostIndex)
