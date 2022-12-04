from django.urls import path
from .views import room,Home

urlpatterns=[
    path("", Home, name="home"),
    path("<str:room_name>/", room, name="room")
]