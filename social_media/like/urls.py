from django.urls import path, include
from social_media.group import views


app_name = 'like'

urlpatterns = [
    # path('', views.GroupListView.as_view(), name='list-group'),
    # path('create/', views.GroupCreateView.as_view(), name='create-group'),
    # path('<slug:slug>/', include([
    #     path('', views.GroupDetailsView.as_view(), name='details-group'),
    #     path('join/', views.GroupJoinGroupView.as_view(), name='join-group'),
    #     path('leave/', views.GroupLeaveGroupView.as_view(), name='leave-group'),
    # ]))
]
