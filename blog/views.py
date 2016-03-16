from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse
from .models import Post

# Create your views here.

class IndexView(generic.ListView):

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.filter(
            published=True
        ).order_by('-pub_date')[:4]


class ArchiveView(generic.ListView):
    model = Post
    template_name = 'blog/archive_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(
            published=True
        ).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Post