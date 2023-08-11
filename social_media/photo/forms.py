from django.forms import ModelForm
from social_media.photo.models import Photo


class PhotoAddForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('photo', 'description',)
