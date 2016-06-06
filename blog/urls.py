from django.conf.urls import url

from . import views
from . import feeds
from .models import Post

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.ArchiveView.as_view(model=Post, date_field='pub_date'), name='index'),
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[0-9|_\-|a-z]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^rss', feeds.LatestPostsFeed())
]