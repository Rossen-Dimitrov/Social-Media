from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import misaka
from django.contrib.auth import get_user_model
from django import template

register = template.Library()

UserModel = get_user_model()


class GroupModel(models.Model):
    GROUP_NAME_MAX_LENGTH = 255

    name = models.CharField(
        max_length=GROUP_NAME_MAX_LENGTH,
        unique=True,
        blank=False,
        null=False,
        )
    slug = models.SlugField(
        allow_unicode=True,
        unique=True,
        editable=False,
    )
    description = models.TextField(
        blank=True,
        default='',
    )
    description_html = models.TextField(
        editable=False,
        default='',
        blank=True,
    )
    members = models.ManyToManyField(UserModel, through='GroupMembersModel')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class GroupMembersModel(models.Model):
    group = models.ForeignKey(GroupModel, related_name='membership', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(UserModel, related_name='user_group', on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('group', 'user')

    def __str__(self):
        return self.user.username