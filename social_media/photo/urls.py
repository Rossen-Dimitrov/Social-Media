from django.urls import path, include
from social_media.photo import views


app_name = 'photo'

urlpatterns = [
    path('add/', views.PhotoAddView.as_view(), name='add-photo'),
    path('<int:pk>/', include([
        path('', views.PhotoDetailsView.as_view(), name='show-photo-details'),
        path('edit/', views.PhotoEditView.as_view(), name='edit-photo'),
    ]))
]
