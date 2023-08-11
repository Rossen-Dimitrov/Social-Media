from django.contrib.auth import get_user_model
from django.db import models

from social_media.photo.models import Photo
from social_media.post.models import Post

UserModel = get_user_model()


class PhotoLike(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)


class PostLike(models.Model):
    to_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
