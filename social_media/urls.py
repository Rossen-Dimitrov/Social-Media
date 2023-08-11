from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("social_media.common.urls", namespace='common')),
    path("accounts/", include("social_media.accounts.urls", namespace='accounts')),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("group/", include("social_media.group.urls", namespace='groups')),
    path("photo/", include("social_media.photo.urls", namespace='photo')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
