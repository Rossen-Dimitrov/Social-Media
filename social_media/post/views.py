from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import Http404
from django.urls import reverse_lazy
from django.views import generic as views
from social_media.post import models, forms
from braces.views import SelectRelatedMixin

UserModel = get_user_model()


class PostCreateView(LoginRequiredMixin, SelectRelatedMixin, views.CreateView):
    fields = ('message', 'group')
    model = models.PostModel
    template_name = 'post/post-add-page.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostListView(SelectRelatedMixin, views.ListView):
    model = models.PostModel
    select_related = ('user', 'group')


class UserPostsListView(views.ListView):
    model = models.PostModel
    template_name = 'post/post-list-page.html'

    def get_queryset(self):
        try:
            self.post_user = UserModel.objects.prefetch_related('posts').get(username_iexact=self.kwargs.get('username'))
        except UserModel.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user

        return context


class PostDetailsView(SelectRelatedMixin, views.DetailView):
    model = models.PostModel
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

    template_name = 'post/post-details-page.html'


class PostEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'post/post-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('accounts:show profile details',
                            kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, SelectRelatedMixin, views.DeleteView):
    model = models.PostModel
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:list-post')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.pk)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)
