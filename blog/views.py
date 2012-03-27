from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from blog.models import *

class PostIndex(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by('-timestamp')

class PostDetail(DetailView):
    model = Post

class ImageList(ListView):
    model = Image

class PostsByTag(PostIndex):
    def get_queryset(self):
        return Post.objects.filter(tags__name__in=[self.kwargs['tag']]).filter(published=True).order_by('-timestamp')

    def get_context_data(self, **kwargs):
        context = super(PostsByTag, self).get_context_data(**kwargs)
        context['current_nav'] = self.kwargs['tag']
        return context

class HomeView(PostIndex):
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['features'] = Feature.objects.filter(active=True).order_by('order')
        context['recent_breaking'] = Post.objects.filter(tags__name__in=['breaking']).filter(published=True).order_by('-timestamp')[:5]
        context['recent_features'] = Post.objects.filter(tags__name__in=['feature']).filter(published=True).order_by('-timestamp')[:5]
        context['recent_favorites'] = Post.objects.filter(tags__name__in=['favorite']).filter(published=True).order_by('-timestamp')[:5]
        return context

class PostsByAuthor(PostIndex):
    def get_queryset(self):
        author = get_object_or_404(User, pk=self.kwargs['user_id'])
        return Post.objects.filter(author=author).filter(published=True).order_by('-timestamp')

@login_required
@csrf_exempt
def new_image(request):

    try:
        i = Image(image = request.FILES['upload'])
        i.save()

        response = "<script type='text/javascript'>"
        response += "window.parent.CKEDITOR.tools.callFunction(%s, '%s');" % (request.GET['CKEditorFuncNum'], i.medium_image.url)
        response += "</script>"

        return HttpResponse(response)
    except:
        return HttpResponse("uhh")
