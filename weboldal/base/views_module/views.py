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


def szofordito2(request):

    def szotar(betuparos):
        # 2 betu
        parosvegbetu = ""
        if betuparos == "sz":
            parosvegbetu = "☿"
        elif betuparos == "cs":
            parosvegbetu = "♆"
        elif betuparos == "zs":
            parosvegbetu = "♆"

        maradekbetu = betuparos[-1]
        if maradekbetu == "¤":
            maradekbetu = ""  # utolso betu eseten tortenik

        betu = betuparos[0]
        vegbetu = ""
        # 1 betu
        if betu == "a":
            vegbetu = "□"
        elif betu == "á":
            vegbetu = "□"
        elif betu == "b":
            vegbetu = "♀"
        elif betu == "c":
            vegbetu = "☾"
        elif betu == "d":
            vegbetu = "♃"
        elif betu == "e":
            vegbetu = "☍"
        elif betu == "é":
            vegbetu = "⚻"  # Quincunx
        elif betu == "f":
            vegbetu = "☿"
        elif betu == "g":
            vegbetu = "☿"
        elif betu == "h":
            vegbetu = "☾"
        elif betu == "i":
            vegbetu = "△"
        elif betu == "í":
            vegbetu = "△"
        elif betu == "j":
            vegbetu = "☉"
        elif betu == "k":
            vegbetu = "☿"
        elif betu == "l":
            vegbetu = "☉"
        elif betu == "m":
            vegbetu = "☽"
        elif betu == "n":
            vegbetu = "☽"
        elif betu == "o":
            vegbetu = "☌"
        elif betu == "ó":
            vegbetu = "⚺"  # Semisextile
        elif betu == "ö":
            vegbetu = "☌"
        elif betu == "ő":
            vegbetu = "⚺"  # Semisextile
        elif betu == "p":
            vegbetu = "♇"
        elif betu == "r":
            vegbetu = "♂"
        elif betu == "s":
            vegbetu = "♂"
        elif betu == "t":
            vegbetu = "♄"
        elif betu == "u":
            vegbetu = "⚹"
        elif betu == "ú":
            vegbetu = "⚺"  # Semisextile
        elif betu == "ü":
            vegbetu = "⚹"
        elif betu == "ű":
            vegbetu = "⚺"  # Semisextile
        elif betu == "v":
            vegbetu = "♂"
        elif betu == "z":
            vegbetu = "♂"
        elif betu == "q":
            vegbetu = "?"
        elif betu == "x":
            vegbetu = "☽"
        elif betu == "y":
            vegbetu = "♀"
        elif betu == "w":
            vegbetu = "♇"

        if parosvegbetu != "":
            return parosvegbetu
        elif vegbetu == "":
            return f"{betu}{maradekbetu}"
        else:
            return f"{vegbetu}{maradekbetu}"

    szo = request.GET.get('input_szo')
    szo = str(szo).lower()
    if len(szo) < 2:
        hibauzenet = "minimum 2 betűsnek kell lennie a megadott szövegnek"
        context = {"forditottszo": "", "szo": "", "hibauzenet": hibauzenet}
        return render(request, 'base/szofordito.html', context)

    vizsgalt_betu = 2
    forditottszo = szotar(f"{szo[0]}{szo[1]}")
    while True:
        forditottszo += szo[vizsgalt_betu]
        forditottszo = forditottszo[:-2] + szotar(f"{forditottszo[-2]}{forditottszo[-1]}")
        vizsgalt_betu += 1

        if len(szo) == vizsgalt_betu:
            forditottszo = forditottszo[:-1] + szotar(f"{forditottszo[-1]}¤")
            break

    forditottszo = forditottszo.replace(" ","   ")
    print(forditottszo)




    context = {"forditottszo": forditottszo, "szo": szo, "atalagitott_f_sz": atalakitott_fsz}
    return render(request, 'base/szofordito.html', context)

def szofordito(request):
    def atalakitas(szo):
        betuparosok =(
                         ("□♀", "♂"),("☍♀", "♂"),("□♂", "♀"),("☍♂", "♀"),
                         ("□☽", "☉"),("☍☽", "☉"),("□☉", "☽"),("☍☉", "☽"),
                            ("□☿", "♃"),("☍☿", "♃"),("□♃", "☿"),("☍♃", "☿")
        )

        for paros in betuparosok:
            szo = szo.replace(paros[0], paros[1])

        return szo

    eredeti_szo = request.GET.get('input_szo')
    if eredeti_szo == None:
        eredeti_szo = "Példa szöveg"
    forditottszo = str(eredeti_szo).lower()
    print("ford1", forditottszo)
    betuparosok = (("sz", "☿"),("cs", "♆"),("zs", "♆"),("a", "□"),("á", "□"),("b", "♀"),("c", "☽"),
     ("d", "♃"),("e", "☍"),("é", "⚻"),("f", "☿"),("g", "☿"),("h", "☽"),("i", "△"),
     ("í", "△"),("j", "☉"),("k", "☿"),("l", "☉"),("m", "☽"),("n", "☽"),("o", "☌"),("ó", "⚺"),
     ("ö", "☌"),("ő", "⚺"),  ("p", "♇"),("r", "♂"),("s", "♂"),("t", "♄"),("u", "⚹"),
     ("ú", "⚺") ,("ü", "⚹"),("ű", "⚺") , ("v", "♂"),("z", "♂"),("q", "?"),("x", "☽"),
     ("y", "♀"),("w", "♇"))

    for paros in betuparosok:
        forditottszo = forditottszo.replace(paros[0], paros[1])


    atalakitott_szo = atalakitas(forditottszo)
    megforditott_eredeti_szo = eredeti_szo[::-1]
    megforditott_forditott_szo = forditottszo[::-1]
    atalakitott_megforditott_szo = atalakitas(megforditott_forditott_szo)

    context = {"eredeti_szo": eredeti_szo,
               "forditottszo": forditottszo,
               "atalakitott_szo": atalakitott_szo,
               "megforditott_eredeti_szo": megforditott_eredeti_szo,
               "megforditott_forditott_szo": megforditott_forditott_szo,
               "atalakitott_megforditott_szo": atalakitott_megforditott_szo
               }

    return render(request, 'base/szofordito.html', context)
