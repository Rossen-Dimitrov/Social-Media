from django.urls import path
from social_media.common import views

app_name = 'common'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home page'),
    path('thanks/', views.ThanksPageView.as_view(), name='thanks page'),
]
