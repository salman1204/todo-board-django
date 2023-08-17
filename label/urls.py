from django.urls import path

from .views import LabelApiView, LabelDetailsApiView

urlpatterns = [
    path("", LabelApiView.as_view()),
    path(
        "<str:label_guid>/",
        LabelDetailsApiView.as_view(),
    ),
]
