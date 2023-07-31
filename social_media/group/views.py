from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views
from social_media.group.models import GroupModel, GroupMembersModel


class GroupCreateView(LoginRequiredMixin, views.CreateView):
    fields = ('name', 'description')
    model = GroupModel
    template_name = 'group/group-add-page.html'


class GroupDetailsView(LoginRequiredMixin, views.DetailView):
    model = GroupModel
    template_name = 'group/group-details-page.html'
    context_object_name = 'group'


class GroupListView(LoginRequiredMixin, views.ListView):
    model = GroupModel
    template_name = 'group/group-list-page.html'


class GroupJoinGroupView(LoginRequiredMixin, views.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('group:group-details', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(GroupModel, slug=self.kwargs.get('slug'))

        try:
            GroupMembersModel.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, 'Already a member!')
        else:
            messages.success(self.request, 'You are now a member')

        return super().get(request, *args, **kwargs)


class GroupLeaveGroupView(LoginRequiredMixin, views.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('group:group-details', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = GroupMembersModel.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug'),
            ).get()
        except GroupMembersModel.DoesNotExist:
            messages.warning(self.request, "Sorry, you are not in this group!")
        else:
            membership.delete()
            messages.success(self.request, "You have left the group!")

        return super().get(request, *args, **kwargs)
