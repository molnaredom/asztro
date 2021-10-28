# ez az apphoz van
from django.urls import path

from . import views
urlpatterns = [
    path("", views.home, name = "home"),
    path("room/<str:pk>/", views.room, name="room"),
    path("create-room/", views.createroom, name= "create-room"),

    path("update-room/<str:pk>/", views.updateRoom, name= "update-room")


    ]