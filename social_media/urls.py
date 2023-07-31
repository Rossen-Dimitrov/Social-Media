from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("social_media.common.urls", namespace='common')),
    path("accounts/", include("social_media.accounts.urls", namespace='accounts')),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("group/", include("social_media.group.urls", namespace='groups')),
    path("post/", include("social_media.post.urls", namespace='posts')),
]
