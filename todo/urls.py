from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("label/", include("label.urls")),
    path("ticket/", include("ticket.urls")),
    # JWT TOken
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]
