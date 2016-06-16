from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag
def get_related(post):
    posts = Post.objects.filter(
        tags__in=post.tags.all()
    ).exclude(
        pk=post.id
    ).distinct()[:3]

    return posts