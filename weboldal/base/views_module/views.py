from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from ..models import Room2, Message2, Horoszkop2, HoroszkopAlapadat
from django.contrib.auth.models import User
from ..forms import RoomForm, HoroszkopFormAutomatic
from django.contrib.auth import authenticate, login, logout
from .horoscope_creator import set_bolygo_es_haz_objektumok


def home(request):
    return render(request, 'base/kezdolap.html', {})


def sorstipus(request):
    return render(request, 'fogalmak_leirasai/sorstipus.html', {})


def anareta(request):
    return render(request, 'fogalmak_leirasai/anareta.html', {})


def celkij_vagy_megval(request):
    return render(request, 'fogalmak_leirasai/celkij_vagy_megval.html', {})


def eletciklusok(request):
    return render(request, 'fogalmak_leirasai/eletciklusok.html', {})


def felosztasok(request):
    return render(request, 'fogalmak_leirasai/felosztasok.html', {})


def hazak_urai(request):
    return render(request, 'fogalmak_leirasai/hazak_urai.html', {})


def serulte_naphold(request):
    return render(request, 'fogalmak_leirasai/serulte_nap_hold.html', {})


def hyleg(request):
    return render(request, 'fogalmak_leirasai/hyleg.html', {})


def room(request, pk):
    room = Room2.objects.get(id=pk)
    room_messages = room.message_set.all().order_by(
        '-created')  # give us a set of messages that are related specific rooms
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message2.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get("body"),
        )
        room.participants.add(request.user)

        return redirect('room', pk=room.id)

    context = {"room": room, "messages": room_messages, 'participants': participants}
    return render(request, "base/room.html", context)


@login_required(login_url="login")
def updateRoom(request, pk):
    room = Room2.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("Nem engedélyezett művelet, amíg nem vagy bejelentkezve")

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {'form': form}
    return render(request, "base/room_form.html", context)


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "HIBA: A felhsználó még nem létezik")

        user = authenticate(request, username=username, password=password)  # hitelesito adatok

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "A Felhasználónév vagy a jelszó nem létezik")

    context = {"page": page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "ERROR: a regisztráció közben")

    return render(request, "base/login_register.html", {'form': form})


def analogia_adatbazis(request):
    context = {}
    return render(request, 'base/analogia_adatbazis.html', context)


def titkosSzoba(request):
    return render(request, "base/titkosSzoba.html", {})


def rolunk(request):
    return render(request, "base/rolunk.html", {})


def fejlesztes_alatt(request):
    return render(request, "base/fejlesztes_alatt.html", {})


def admin_panel(request):

    if request.method == "POST":
        if 'osszeshoroszkopujra' in request.POST:
            sure = input("Biztosan törölni szeretnéd az összes horoszkópot és újratölteni? (yes/no)")
            if sure == "yes" or sure == "y":
                Horoszkop2.objects.all().delete()

                horoszkop_alapadatok = HoroszkopAlapadat.objects.all()
                for hp_alap in horoszkop_alapadatok:
                    print(hp_alap)
                    form = HoroszkopFormAutomatic()
                    obj = form.save(commit=False)
                    obj.tulajdonos_neve = hp_alap.tulajdonos_neve
                    obj.idopont = hp_alap.idopont
                    obj.hely = hp_alap.hely
                    obj.tipus = hp_alap.tipus
                    obj.neme = hp_alap.neme
                    obj.leirasok = hp_alap.leirasok
                    obj.munka = hp_alap.munka

                    obj = set_bolygo_es_haz_objektumok(obj)

                    obj.save()


                return redirect(f"horoszkop_gyujtemeny")

        elif "mentes_es_foolal" in request.POST:
            return redirect(f"horoszkop_gyujtemeny")

    return render(request, "base/admin_panel.html", {})
