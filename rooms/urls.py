from django.urls import path
from .views import *

app_name = "rooms"

urlpatterns = [
    path("", ListRoomView.as_view()),
    path("<int:pk>/", SeeRoomView.as_view()),
]
