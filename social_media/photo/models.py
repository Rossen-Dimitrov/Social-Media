from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse

from social_media.group.models import GroupModel
from validators import MaxFileSizeValidator

UserModel = get_user_model()


class Photo(models.Model):
    MAX_DESCRIPTION_LENGTH = 300
    MIN_DESCRIPTION_LENGTH = 10

    IMAGE_MAX_SIZE_IN_MB = 5

    photo = models.ImageField(
        validators=(
            MaxFileSizeValidator(IMAGE_MAX_SIZE_IN_MB),
        ),
        null=False,
        blank=True
    )
    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        related_name='photo',
        on_delete=models.SET_NULL,
        null=True
    )
    group = models.ForeignKey(
        GroupModel,
        related_name='photo',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    date_of_publication = models.DateField(
        auto_now=True
    )

    @staticmethod
    def get_absolute_url():
        return reverse('common:home page')
