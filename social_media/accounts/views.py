from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login
from social_media.accounts import forms
from social_media.accounts.forms import LoginForm

UserModel = get_user_model()


class ProfileRegisterView(views.CreateView):
    model = UserModel
    form_class = forms.AppUserRegisterForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('common:home-page')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)

            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form})


class ProfileLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'


class ProfileLogoutView(LoginRequiredMixin, auth_views.LogoutView):
    pass


class ProfileDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/profile-details-page.html'


class ProfileEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('accounts:show-profile-details',
                            kwargs={'pk': self.object.pk})


class ProfileDeleteView(LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/profile-delete-page.html'
