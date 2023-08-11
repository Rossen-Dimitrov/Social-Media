from django.urls import path, include
from social_media.post import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list-post'),
    path('<slug:group_slug>/<int:user_id>/', include([
        path('', views.PostDetailsView.as_view(), name='post-details'),
        path('create/', views.post_create_view, name='create-post'),
        path('user_posts_list/', views.UserPostsListView.as_view(), name='show-all-user-post'),
        path('edit/', views.PostEditView.as_view(), name='edit-post'),
        path('delete/', views.PostDeleteView.as_view(), name='delete-post'),
    ]))
]