from django.contrib import admin
from social_media.post.models import Post


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'group')
