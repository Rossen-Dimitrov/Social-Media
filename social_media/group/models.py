from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import misaka
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class GroupModel(models.Model):
    GROUP_NAME_MAX_LENGTH = 255

    name = models.CharField(
        max_length=GROUP_NAME_MAX_LENGTH,
        unique=True,
        blank=False,
        null=False,
        verbose_name=_("Name"),
    )
    slug = models.SlugField(
        allow_unicode=True,
        unique=True,
        editable=False,
    )
    description = models.TextField(
        blank=True,
        default='',
        verbose_name=_("Description"),
    )
    description_html = models.TextField(
        editable=False,
        default='',
        blank=True,
    )
    members = models.ManyToManyField(UserModel, through='GroupMembersModel', verbose_name=_("Members"))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify(f"{self.name}-{self.id}")
        self.description_html = misaka.html(self.description)

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:details-group', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")


class GroupMembersModel(models.Model):
    group = models.ForeignKey(GroupModel, related_name='membership', on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, related_name='group_member', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('group', 'user')
        verbose_name = _("Group Member")
        verbose_name_plural = _("Group Members")

    def __str__(self):
        return self.user.username
