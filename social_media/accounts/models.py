from django.contrib.auth import models as auth_models
from django.db import models
from django.core import validators
from validators import validate_letters_only


class AppUser(auth_models.AbstractUser, auth_models.PermissionsMixin):
    MIN_FIRST_NAME_LEN = 2
    MAX_FIRST_NAME_LEN = 30
    MIN_LAST_NAME_LEN = 2
    MAX_LAST_NAME_LEN = 30

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    username = models.CharField(
        max_length=MAX_FIRST_NAME_LEN,
        validators=(
            validators.MinLengthValidator(MIN_FIRST_NAME_LEN),
        ),
        unique=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LEN,
        validators=(
            validators.MinLengthValidator(MIN_FIRST_NAME_LEN),
            validate_letters_only,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LEN,
        validators=(
            validators.MinLengthValidator(MIN_LAST_NAME_LEN),
            validate_letters_only,
        ),
        null=False,
        blank=False,
    )

    profile_img = models.ImageField(
        default='profileimages/person.png',
        upload_to='profileimages/',
        null=True,
        blank=True,
    )
    last_login = models.DateTimeField(
        auto_now=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"
