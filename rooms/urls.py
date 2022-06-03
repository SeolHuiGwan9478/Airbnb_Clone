from django.urls import path
from .views import *

app_name = "rooms"

urlpatterns = [
    path("list/", list_rooms),
]
