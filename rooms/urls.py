from django.urls import path
from .views import *

app_name = "rooms"

urlpatterns = [
    path("", RoomsView.as_view()),
    path("<int:pk>/", RoomView.as_view()),
]
