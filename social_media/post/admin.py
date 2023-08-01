from django.contrib import admin
from social_media.post.models import PostModel


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'group')
