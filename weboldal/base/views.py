from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic, Jegy_1, Bolygo_1, Haz_1, Message ,BolygoHazban_1, BolygoJegyben_1, HazJegyben_1
from .forms import RoomForm, AnalogiaForm, JegyekForm, BolygokForm, HazakForm , BolygoJegybenForm, HazJegybenForm, BolygoHazbanForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# rooms = [
#
#     {'id': 1 , "name":"Edgár"},
#     {'id': 2 , "name":"Elen"},
#     {'id': 3 , "name":"Póó"}
#
# ]


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(discription__icontains=q)

    )

    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms': rooms, "topics":topics, "room_count":room_count}
    return render(request, 'base/home.html', context )


def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created') # give us a set of messages that are related specific rooms
    participants = room.participants.all()
    print(len(room_messages))
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get("body"),
        )
        room.participants.add(request.user)

        return redirect('room', pk=room.id)

    context = {"room": room, "messages": room_messages, 'participants': participants}
    return render(request, "base/room.html",context)

@login_required(login_url="login")
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("Nem engedélyezett művelet, amíg nem vagy bejelentkezve")

    if request.method == "POST":
        message.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj":message})

@login_required(login_url="login")
def createroom(request):
    form = RoomForm()

    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            return redirect("home")

    context = {'form': form}
    return render(request, "base/room_form.html", context)


@login_required(login_url="login")
def updateRoom( request, pk):
    room = Room.objects.get(id= pk)
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


@login_required(login_url="login")
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("Nem engedélyezett művelet, amíg nem vagy bejelentkezve")

    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj":room})



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
            messages.error(request , "HIBA: A felhsználó még nem létezik")

        user = authenticate(request, username= username, password= password) # hitelesito adatok

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






def analogia(request,nevID):
    analogia = Jegy_1.objects.get(nevID=nevID)

    context = {"analogia": analogia} # ez egy objektum

    return render(request,"analogiak/analogia.html", context )


def createAnalogia(request):
    form = AnalogiaForm()

    if request.method == "POST":
        form = AnalogiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("analogia_adatbazis")

    context = {'form': form}
    return render(request, "analogiak/analogia_form.html", context)


def analogia_adatbazis(request):


    context = {}
    return render(request, 'analogiak/analogia_adatbazis.html', context )




# konkrét oldalak( a fa levelei)
def jegy(request,nevID):
    analogia = Jegy_1.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "analogiak/jegy.html", context)


def bolygo(request,nevID):
    analogia = Bolygo_1.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "analogiak/bolygo.html", context)


def haz(request,nevID):
    analogia = Haz_1.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "analogiak/haz.html", context)


def bolygoJegyben(request,osszetett_nevID):
    analogia = BolygoJegyben_1.objects.get(osszetett_nevID=osszetett_nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "osszetettAnalogiak/bolygoJegyben.html", context)


def bolygoHazban(request,osszetett_nevID):
    analogia = BolygoHazban_1.objects.get(osszetett_nevID=osszetett_nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "osszetettAnalogiak/bolygoHazban.html", context)


def hazJegyben(request,osszetett_nevID):
    analogia = HazJegyben_1.objects.get(osszetett_nevID=osszetett_nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "osszetettAnalogiak/hazJegyben.html", context)






# több oldalt tartalmazo,analógiatároló felület
def jegyek_oldal(request):

    jegyek = Jegy_1.objects.all()

    context = {'adatok': jegyek}
    return render(request, 'analogiak/jegyek.html', context )


def bolygok_oldal(request):

    bolygok = Bolygo_1.objects.all()

    context = {'adatok': bolygok}
    return render(request, 'analogiak/bolygok.html', context )


def hazak_oldal(request):

    hazak = Haz_1.objects.all()

    context = {'adatok': hazak}
    return render(request, 'analogiak/hazak.html', context )


def bolygokJegyekben(request):

    jegyek = BolygoJegyben_1.objects.all()

    context = {'adatok': jegyek}
    return render(request, 'osszetettAnalogiak/bolygokJegyekben.html', context )


def bolygokHazakban(request):

    bolygok = BolygoHazban_1.objects.all()

    context = {'adatok': bolygok}
    return render(request, 'osszetettAnalogiak/bolygokHazakban.html', context )


def hazakJegyekben(request):

    hazak = HazJegyben_1.objects.all()
    print("----------",hazak)
    context = {'adatok': hazak}
    return render(request, 'osszetettAnalogiak/hazakJegyekben.html', context )





#createrek
def createJegyek(request):
    form = JegyekForm()

    if request.method == "POST":
        form = JegyekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("jegyek")

    context = {'form': form}
    return render(request, "analogiak/jegyek_form.html", context)


def createBolygok(request):
    form = BolygokForm()

    if request.method == "POST":
        form = BolygokForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bolygok")

    context = {'form': form}
    return render(request, "analogiak/bolygok_form.html", context)


 #job lib

def createHazak(request):
    form = HazakForm()

    if request.method == "POST":
        form = HazakForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hazak")

    context = {'form': form}
    return render(request, "analogiak/hazak_form.html", context)


def createBolygoJegyben(request):
    form = BolygoJegybenForm()

    if request.method == "POST":
        form = BolygoJegybenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bolygokJegyekben")

    context = {'form': form}
    return render(request, "osszetettAnalogiak/bolygoJegyben_form.html", context)


def createBolygoHazban(request):
    form = BolygoHazbanForm()

    if request.method == "POST":
        form = BolygoHazbanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bolygokHazakban")

    context = {'form': form}
    return render(request, "osszetettAnalogiak/bolygoHazban_form.html", context)


 #job lib

def createHazJegyben(request):
    form = HazJegybenForm()

    if request.method == "POST":
        form = HazJegybenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hazakJegyekben")

    context = {'form': form}
    return render(request, "osszetettAnalogiak/hazJegyben_form.html", context)



#deleterek
def deleteBolygo(request, nevID):
    bolygo = Bolygo_1.objects.get(nevID=nevID)
    if request.method == "POST":
        bolygo.delete()
        return redirect("bolygok")
    return render(request, "base/delete.html", {"obj":bolygo})


def deleteJegy(request, nevID):
    jegy = Jegy_1.objects.get(nevID=nevID)
    if request.method == "POST":
        jegy.delete()
        return redirect("jegyek")
    return render(request, "base/delete.html", {"obj":jegy})


def deleteHaz(request,nevID):
    haz = Haz_1.objects.get(nevID=nevID)
    if request.method == "POST":
        haz.delete()
        return redirect("hazak")
    return render(request, "base/delete.html", {"obj":haz})


def deleteBolygoJegyben(request, nevID):
    bolygo = BolygoJegyben_1.objects.get(nevID=nevID)
    if request.method == "POST":
        bolygo.delete()
        return redirect("bolygokJegyekben")
    return render(request, "base/delete.html", {"obj":bolygo})


def deleteBolygoHazban(request, nevID):
    jegy = BolygoHazban_1.objects.get(nevID=nevID)
    if request.method == "POST":
        jegy.delete()
        return redirect("bolygokHazakban")
    return render(request, "base/delete.html", {"obj":jegy})


def deleteHazJegyben(request,nevID):
    haz = HazJegyben_1.objects.get(nevID=nevID)
    if request.method == "POST":
        haz.delete()
        return redirect("hazakJegyekben")
    return render(request, "base/delete.html", {"obj":haz})






def titkosSzoba(request):
    return render(request, "analogiak/titkosSzoba.html", {})




# def updateAnalogia(request, nevID):
#     analogia = Analogia.objects.get(id=nevID)
#     form = AnalogiaForm(instance=analogia)
#
#     if request.method == 'POST':
#         form = RoomForm(request.POST, instance=room)
#         if form.is_valid():
#             form.save()
#             return redirect("home") #todo ne homrea terjen vissza
#
#     context = {'form': form}
#     return render(request, "base/room_form.html", context)