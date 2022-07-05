from django.urls import path

from .views_module import horoscope_creator, views_deleters, views, views_creators, views, \
    views_horoszkop_elemzes, views_konkret_analogia, views_updaters, views_analogiatarolok
from . import views_analogia_gyakorlo
from .ml_oldal import ml

egyedi_oldalak = [
    path("titkos-szoba/", views.titkosSzoba, name="titkos-szoba"),
    path("", views.home, name="home"),
    path("rolunk", views.rolunk, name="rolunk"),
    path("szofordito", views.szofordito, name="szofordito"),
    path("fejlesztes_alatt", views.fejlesztes_alatt, name="fejlesztes_alatt"),
    path("admin_panel", views.admin_panel, name="admin_panel"),
    path("pontositas", views.pontositas, name="pontositas"),
]

analogia_tarolok = [
    path("horoszkop_gyujtemeny/", views_analogiatarolok.horoszkop_gyujtemeny, name="horoszkop_gyujtemeny"),
    path("bolygokJegyekben/", views_analogiatarolok.bolygokJegyekben, name="bolygokJegyekben"),
    path("bolygokHazakban/", views_analogiatarolok.bolygokHazakban, name="bolygokHazakban"),
    path("hazakJegyekben/", views_analogiatarolok.hazakJegyekben, name="hazakJegyekben"),
    path("hazakUraHazakban/", views_analogiatarolok.hazakUraHazakban, name="hazakUraHazakban"),
    path("jegyek/", views_analogiatarolok.jegyek_oldal, name="jegyek"),
    path("hazak/", views_analogiatarolok.hazak_oldal, name="hazak"),
    path("bolygok/", views_analogiatarolok.bolygok_oldal, name="bolygok"),
    path("analogia_adatbazis/", views.analogia_adatbazis, name="analogia_adatbazis"),
]

konkret_analogiak = [
    path("horoszkop/<str:id>/", views_horoszkop_elemzes.horoszkop, name="horoszkop"),
    path("bolygoJegyben/<str:id>/", views_konkret_analogia.bolygoJegyben, name="bolygoJegyben"),  # ~room
    path("bolygoHazban/<str:id>/", views_konkret_analogia.bolygoHazban, name="bolygoHazban"),  # ~room
    path("hazJegyben/<str:id>/", views_konkret_analogia.hazJegyben, name="hazJegyben"),  # ~room
    path("hazUraHazban/<str:id>/", views_konkret_analogia.hazUraHazban, name="hazUraHazban"),  # ~room
    path("jegy/<str:nevID>/", views_konkret_analogia.jegy, name="jegy"),
    path("haz/<str:nevID>/", views_konkret_analogia.haz, name="haz"),
    path("bolygo/<str:nevID>/", views_konkret_analogia.bolygo, name="bolygo"),
]

updaterek = [

    path("update-jegy/<str:nevID>/", views_updaters.updateJegy, name="update-jegy"),
    path("update-bolygo/<str:nevID>/", views_updaters.updateBolygo, name="update-bolygo"),
    path("update-haz/<str:nevID>/", views_updaters.updateHaz, name="update-haz"),
    path("update-horoszkop/<str:id>/", views_updaters.updateHoroszkop, name="update-horoszkop"),
    path("update-bolygoJegyben/<str:id>/", views_updaters.updateBolygoJegyben, name="update-bolygoJegyben"),
    path("update-hazJegyben/<str:id>/", views_updaters.updateHazJegyben, name="update-hazJegyben"),
    path("update-bolygoHazban/<str:id>/", views_updaters.updateBolygoHazban, name="update-bolygoHazban"),
    path("update-hazUraHazban/<str:id>/", views_updaters.updateHazUraHazban, name="update-hazUraHazban"),

]

machine_learning = [
    path("ml_fooldal/", ml.ml_fooldal, name="ml_fooldal"),
    path("generalt_adatok/", ml.generalt_adatok, name="generalt_adatok"),

]

hasznalaton_kivul = [
    path("create-room/", views_creators.createroom, name="create-room"),
    path("update-room/<str:pk>/", views.updateRoom, name="update-room"),
    path("delete-room/<str:pk>/", views_deleters.deleteRoom, name="delete-room"),
    path("delete-message/<str:pk>/", views_deleters.deleteMessage, name="delete-message"),
    path("room/<str:pk>/", views.room, name="room"),
]

create_analogiak = [
    path("create-horoszkop/", horoscope_creator.createHoroszkopGyors, name="create-horoszkop"),
    path("create-bolygoJegyben/", views_creators.createBolygoJegyben, name="create-bolygoJegyben"),
    path("create-bolygoHazban/", views_creators.createBolygoHazban, name="create-bolygoHazban"),
    path("create-hazJegyben/", views_creators.createHazJegyben, name="create-hazJegyben"),
    path("create-hazUraHazban/", views_creators.createHazUraHazban, name="create-hazUraHazban"),
    path("create-jegyek/", views_creators.createJegyek, name="create-jegyek"),
    path("create-hazak/", views_creators.createHazak, name="create-hazak"),
    path("create-bolygok/", views_creators.createBolygok, name="create-bolygok"),
]

deleterek = [
    path("delete-horoszop/<str:id>/", views_deleters.deleteHoroszkop, name="delete-horoszkop"),
    path("delete-jegy/<str:nevID>/", views_deleters.deleteJegy, name="delete-jegy"),
    path("delete-haz/<str:nevID>/", views_deleters.deleteHaz, name="delete-haz"),
    path("delete-bolygo/<str:nevID>/", views_deleters.deleteBolygo, name="delete-bolygo"),
    path("delete-bolygoJegyben/<str:id>/", views_deleters.deleteBolygoJegyben, name="delete-bolygoJegyben"),
    path("delete-hazJegyben/<str:id>/", views_deleters.deleteHazJegyben, name="delete-hazJegyben"),
    path("delete-bolygoHazban/<str:id>/", views_deleters.deleteBolygoHazban, name="delete-bolygoHazban"),
    path("delete-hazUraHazban/<str:id>/", views_deleters.deleteHazUraHazban, name="delete-hazUraHazban"),

]

felhasznalokezeles = [
    path("login", views.loginPage, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("register", views.registerPage, name="register"),
]


gyakorlo = [
    path("gyakorlo/", views_analogia_gyakorlo.index, name="index"),
    path("gyakorlo/<int:myid>/", views_analogia_gyakorlo.quiz, name="quiz"),
    path('gyakorlo/<int:myid>/data/', views_analogia_gyakorlo.quiz_data_view, name='quiz-data'),
    path('gyakorlo/<int:myid>/save/', views_analogia_gyakorlo.save_quiz_view, name='quiz-save'),

    path('add_quiz/', views_analogia_gyakorlo.add_quiz, name='add_quiz'),
    path('add_question/', views_analogia_gyakorlo.add_question, name='add_question'),
    path('add_options/<int:myid>/', views_analogia_gyakorlo.add_options, name='add_options'),
    path('results/', views_analogia_gyakorlo.results, name='results'),
    path('delete_question/<int:myid>/', views_analogia_gyakorlo.delete_question, name='delete_question'),
    path('delete_result/<int:myid>/', views_analogia_gyakorlo.delete_result, name='delete_result'),
]

fogalmak = [
    path('fogalmak/sorstipus/', views.sorstipus, name='sorstipus'),
    path('fogalmak/hazak_urai/', views.hazak_urai, name='hazak_urai'),
    path('fogalmak/anareta/', views.anareta, name='anareta'),
    path('fogalmak/eletciklusok/', views.eletciklusok, name='eletciklusok'),
    path('fogalmak/celkij_vagy_megval/', views.celkij_vagy_megval, name='celkij_vagy_megval'),
    path('fogalmak/felosztasok/', views.felosztasok, name='felosztasok'),
    path('fogalmak/serulte_naphold/', views.serulte_naphold, name='serulte_naphold'),
    path('fogalmak/hyleg/', views.hyleg, name='hyleg'),
]

urlpatterns = []

urlpatterns += hasznalaton_kivul
urlpatterns += create_analogiak
urlpatterns += felhasznalokezeles
urlpatterns += analogia_tarolok
urlpatterns += konkret_analogiak
urlpatterns += deleterek
urlpatterns += updaterek
urlpatterns += machine_learning
urlpatterns += egyedi_oldalak
urlpatterns += gyakorlo
urlpatterns += fogalmak




