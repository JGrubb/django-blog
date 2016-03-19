from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Post, Tag
from django.contrib.sitemaps import Sitemap


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


class TagsView(generic.ListView):
    template_name = 'blog/archive_list.html'

    def get_queryset(self):
        self.term = get_object_or_404(Tag, slug=self.args[0])
        return Post.objects.filter(tags=self.term).order_by('-pub_date')

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.filter(published=True).order_by('-pub_date')

    def lastmod(self, obj):
        return obj.pub_date