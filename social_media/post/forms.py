from django import forms
from social_media.post import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["message"]
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Write your post...'})
        }

