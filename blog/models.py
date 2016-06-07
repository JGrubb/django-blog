from __future__ import unicode_literals
from django.utils import timezone

from django.db import models
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):

    def prev_post_choices(pub_date):
        return {
            'pub_date__lte': pub_date
        }

    title = models.CharField(max_length=255)
    body = models.TextField()
    summary = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255)
    pub_date = models.DateTimeField('Published at')
    published = models.BooleanField()
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    previous = models.OneToOneField('self',
                                 related_name='previous_post',
                                 blank=True,
                                 null=True,
                                 on_delete=None)

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog:detail', [self.id, self.slug])

    class Meta:
        ordering = ['-pub_date']

