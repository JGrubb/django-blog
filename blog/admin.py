from django.contrib import admin

# Register your models here.

from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'pub_date', 'published')
    filter_horizontal = ('tags',)

admin.site.register(Post, PostAdmin)