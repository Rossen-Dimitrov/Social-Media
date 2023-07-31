from django import forms

from social_media.post import models


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("message", "group")
        model = models.PostModel

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["group"].queryset = (
                models.GroupModel.objects.filter(
                    pk__in=user.groups.values_list("group__pk")
                )
            )
