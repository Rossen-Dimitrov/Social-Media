from django.urls import path, include
from social_media.accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.ProfileRegisterView.as_view(), name='register-user'),
    path('login/', views.ProfileLoginView.as_view(), name='login-user'),
    path('logout/', views.ProfileLogoutView.as_view(), name='logout-user'),
    path('profile/<int:pk>/', include([
        path('', views.ProfileDetailsView.as_view(), name='show-profile-details'),
        path('edit/', views.ProfileEditView.as_view(), name='edit-profile'),
        path('delete/', views.ProfileDeleteView.as_view(), name='delete-profile'),
    ]))
]