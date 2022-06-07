from django.urls import path
from .views import *

app_name = "rooms"

urlpatterns = [
    path("", rooms_view),
    path("<int:pk>/", SeeRoomView.as_view()),
]
