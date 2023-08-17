from django.urls import path

from .views import (TicketApiView, TicketDetailsApiView, TicketExpireToday,
                    TicketTrackHistoryDetailsApiView)

urlpatterns = [
    path("", TicketApiView.as_view()),
    path("expire-today", TicketExpireToday.as_view()),

    path(
        "<str:ticket_guid>/",
        TicketDetailsApiView.as_view(),
    ),
    path(
        "history/<str:ticket_guid>/",
        TicketTrackHistoryDetailsApiView.as_view(),
    ),
]
