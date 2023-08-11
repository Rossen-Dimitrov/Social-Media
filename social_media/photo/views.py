from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from django.views import generic as views

from social_media.photo.forms import PhotoAddForm
from social_media.photo.models import Photo


class PhotoAddView(LoginRequiredMixin, views.CreateView):
    form_class = PhotoAddForm
    model = Photo
    template_name = 'photo/photo-add-page.html'


class PhotoEditView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ('photo', 'description',)
    template_name = 'photo/photo-edit-page.html'


class PhotoDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'photo/photo-details-page.html'


