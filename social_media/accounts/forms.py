from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField

UserModel = get_user_model()


class AppUserRegisterForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        fields = ('username', 'email', 'password1', 'password2', 'profile_img')
        model = UserModel

    # labels = {
    #     'username': 'Enter Your Name',
    #     'email': 'Enter Email Address',
    #     'password1': 'Enter password',
    #     'password2': 'Repeat password',
    # }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, "placeholder": "username"}))
    password = forms.CharField(strip=False,
                               widget=forms.PasswordInput(
                                   attrs={"autocomplete": "current-password", "placeholder": "Password"}))














