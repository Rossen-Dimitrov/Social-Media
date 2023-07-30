from django.contrib import admin
from social_media.group.models import GroupModel


@admin.register(GroupModel)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')
