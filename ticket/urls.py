from django.urls import path

from .views import TicketApiView

urlpatterns = [
    path("", TicketApiView.as_view()),
]
