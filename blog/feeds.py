from django.contrib.syndication.views import Feed
from .models import Post
from blog.templatetags.markdownify import markdown

class LatestPostsFeed(Feed):

    title = "Ignored by dinosaurs"
    link = '/posts/'
    description = "Thoughts from my brain."

    def items(self):
        return Post.objects.filter(published=True).order_by('-pub_date')[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return markdown(item.body)