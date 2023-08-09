from django.urls import path

from .views import LabelApiView

urlpatterns = [
    path("", LabelApiView.as_view()),
]
