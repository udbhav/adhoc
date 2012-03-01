from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

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
        return Post.objects.filter(tags__name__in=[self.kwargs['tag']]).filter(published=True).order_by('timestamp')

    def get_context_data(self, **kwargs):
        context = super(PostsByTag, self).get_context_data(**kwargs)
        context['current_nav'] = self.kwargs['tag']
        return context



class HomeView(PostIndex):
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['features'] = Feature.objects.filter(active=True).order_by('order')
        return context


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
