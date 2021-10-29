# ez az apphoz van
from django.urls import path


from . import views
urlpatterns = [
    path("", views.home, name = "home"),
    path("room/<str:pk>/", views.room, name="room"),

    path("create-room/", views.createroom, name= "create-room"),
    path("update-room/<str:pk>/", views.updateRoom, name= "update-room"),
    path("delete-room/<str:pk>/", views.deleteRoom, name= "delete-room"),

    path("login", views.loginPage, name= "login"),
    path("logout", views.logoutUser, name= "logout"),





    path("analogia_adatbazis/", views.analogia_adatbazis, name= "analogia_adatbazis"),  # ~home
    path("analogia/<str:nevID>/", views.analogia, name="analogia"),  # ~room
    path("create-analogia/", views.createAnalogia, name= "create-analogia"),

    path("jegyek/", views.jegyek_oldal, name= "jegyek"),
    path("hazak/", views.hazak_oldal, name= "hazak"),
    path("bolygok/", views.bolygok_oldal, name= "bolygok"),

    path("create-jegyek/", views.createJegyek, name= "create-jegyek"),
    path("create-hazak/", views.createHazak, name= "create-hazak"),
    path("create-bolygok/", views.createBolygok, name= "create-bolygok"),

    path("jegy/<str:nevID>/", views.jegy, name="jegy"),  # ~room
    path("haz/<str:nevID>/", views.haz, name="haz"),  # ~room
    path("bolygo/<str:nevID>/", views.bolygo, name="bolygo"),  # ~room

    path("delete-jegy/<str:nevID>/", views.deleteJegy, name= "delete-jegy"),
    path("delete-haz/<str:nevID>/", views.deleteHaz, name= "delete-haz"),
    path("delete-bolygo/<str:nevID>/", views.deleteBolygo, name= "delete-bolygo"),

    ]




