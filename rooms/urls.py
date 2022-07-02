from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

app_name = "rooms"
router = DefaultRouter()
router.register("", RoomViewSet)

urlpatterns = router.urls
