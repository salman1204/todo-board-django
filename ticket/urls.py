from django.urls import path

from .views import TicketApiView, TicketDetailsApiView

urlpatterns = [
    path("", TicketApiView.as_view()),
    path(
        "<str:ticket_guid>/",
        TicketDetailsApiView.as_view(),
    ),
]
