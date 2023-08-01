from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse, reverse_lazy

import misaka

from social_media.group.models import GroupModel

UserModel = get_user_model()


class PostModel(models.Model):
    user = models.ForeignKey(
        UserModel,
        related_name='posts',
        on_delete=models.SET_NULL,
        null=True
        )
    date_created = models.DateTimeField(
        auto_now=True
    )
    message = models.TextField()
    message_html = models.TextField(
        editable=False,
    )
    group = models.ForeignKey(
        GroupModel,
        related_name='posts',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('posts:post-details', kwargs={'username': self.user.username, 'pk': self.pk})

    class Meta:
        ordering = ['-date_created']
        unique_together = ['user', 'message']
