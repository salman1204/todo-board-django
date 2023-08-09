from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),

    # JWT TOken
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
