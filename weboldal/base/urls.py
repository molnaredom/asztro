# ez az apphoz van
from django.urls import path

from . import views
urlpatterns = [
    path("", views.home, name = "home"),
    path("room/<str:pk>/", views.room, name="room"),
    path("create-room/", views.createroom, name= "create-room"),

    path("update-room/<str:pk>/", views.updateRoom, name= "update-room"),
    path("delete-room/<str:pk>/", views.deleteRoom, name= "delete-room"),

    path("analogia_adatbazis/", views.analogia_adatbazis, name= "analogia_adatbazis"),  # ~home
    path("analogia/<str:nevID>/", views.analogia, name="analogia"),  # ~room
    path("create-analogia/", views.createAnalogia, name= "create-analogia"),




    ]