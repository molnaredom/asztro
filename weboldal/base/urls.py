# ez az apphoz van
from django.urls import path


from . import views, views_creators, views_deleters, views_analogiatarolok,views_konkret_analogia, views_updaters
from . import views_horoszkop_elemzes


urlpatterns = [
    path("", views.home, name = "home"),
    path("room/<str:pk>/", views.room, name="room"),
    path("rolunk", views.rolunk, name="rolunk"),
    path("analogiagyakorlo", views.analogiagyakorlo, name="analogiagyakorlo"),

    path("create-room/", views_creators.createroom, name= "create-room"),
    path("update-room/<str:pk>/", views.updateRoom, name= "update-room"),
    path("delete-room/<str:pk>/", views_deleters.deleteRoom, name= "delete-room"),
    path("delete-message/<str:pk>/", views_deleters.deleteMessage, name= "delete-message"),

    path("login", views.loginPage, name= "login"),
    path("logout", views.logoutUser, name= "logout"),
    path("register", views.registerPage, name= "register"),


    path("analogia_adatbazis/", views.analogia_adatbazis, name= "analogia_adatbazis"),  # ~home
    # path("analogia/<str:nevID>/", views.analogia, name="analogia"),  # ~room
    # path("create-analogia/", views.createAnalogia, name= "create-analogia"),

    path("jegyek/", views_analogiatarolok.jegyek_oldal, name= "jegyek"),
    path("hazak/", views_analogiatarolok.hazak_oldal, name= "hazak"),
    path("bolygok/", views_analogiatarolok.bolygok_oldal, name= "bolygok"),

    path("create-jegyek/", views_creators.createJegyek, name= "create-jegyek"),
    path("create-hazak/", views_creators.createHazak, name= "create-hazak"),
    path("create-bolygok/", views_creators.createBolygok, name= "create-bolygok"),

    path("jegy/<str:nevID>/", views_konkret_analogia.jegy, name="jegy"),
    path("haz/<str:nevID>/", views_konkret_analogia.haz, name="haz"),
    path("bolygo/<str:nevID>/", views_konkret_analogia.bolygo, name="bolygo"),

    path("delete-jegy/<str:nevID>/", views_deleters.deleteJegy, name= "delete-jegy"),
    path("delete-haz/<str:nevID>/", views_deleters.deleteHaz, name= "delete-haz"),
    path("delete-bolygo/<str:nevID>/", views_deleters.deleteBolygo, name= "delete-bolygo"),


    path("bolygokJegyekben/", views_analogiatarolok.bolygokJegyekben, name= "bolygokJegyekben"),
    path("bolygokHazakban/", views_analogiatarolok.bolygokHazakban, name= "bolygokHazakban"),
    path("hazakJegyekben/", views_analogiatarolok.hazakJegyekben, name= "hazakJegyekben"),

    path("create-bolygoJegyben/", views_creators.createBolygoJegyben, name= "create-bolygoJegyben"),
    path("create-bolygoHazban/", views_creators.createBolygoHazban, name= "create-bolygoHazban"),
    path("create-hazJegyben/", views_creators.createHazJegyben, name= "create-hazJegyben"),

    path("bolygoJegyben/<str:id>/", views_konkret_analogia.bolygoJegyben, name="bolygoJegyben"),  # ~room
    path("bolygoHazban/<str:id>/", views_konkret_analogia.bolygoHazban, name="bolygoHazban"),  # ~room
    path("hazJegyben/<str:id>/", views_konkret_analogia.hazJegyben, name="hazJegyben"),  # ~room

    path("delete-bolygoJegyben/<str:id>/", views_deleters.deleteBolygoJegyben, name= "delete-bolygoJegyben"),
    path("delete-hazJegyben/<str:id>/", views_deleters.deleteHazJegyben, name= "delete-hazJegyben"),
    path("delete-bolygoHazban/<str:id>/", views_deleters.deleteBolygoHazban, name= "delete-bolygoHazban"),

    path("horoszkop_gyujtemeny/", views_analogiatarolok.horoszkop_gyujtemeny, name="horoszkop_gyujtemeny"),
    path("create-horoszkop/", views_creators.createHoroszkop, name= "create-horoszkop"),
    path("delete-horoszop/<str:id>/", views_deleters.deleteHoroszkop, name= "delete-horoszkop"),

    path("horoszkop/<str:id>/", views_horoszkop_elemzes.horoszkop, name="horoszkop"),


    path("update-jegy/<str:nevID>/", views_updaters.updateJegy, name= "update-jegy"),
    path("update-bolygo/<str:nevID>/", views_updaters.updateBolygo, name= "update-bolygo"),
    path("update-haz/<str:nevID>/", views_updaters.updateHaz, name= "update-haz"),
    path("update-horoszkop/<str:id>/", views_updaters.updateHoroszkop, name= "update-horoszkop"),
    path("update-bolygoJegyben/<str:id>/", views_updaters.updateBolygoJegyben, name= "update-bolygoJegyben"),
    path("update-hazJegyben/<str:id>/", views_updaters.updateHazJegyben, name= "update-hazJegyben"),
    path("update-bolygoHazban/<str:id>/", views_updaters.updateBolygoHazban, name= "update-bolygoHazban"),

    path("titkos-szoba/", views.titkosSzoba, name="titkos-szoba"),




    ]




