from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.ArchiveView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[0-9|_\-|a-z]+)/$', views.DetailView.as_view(), name='detail'),

]