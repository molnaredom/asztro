from django.shortcuts import render

rooms = [

    {'id': 1 , "name":"Edgár"},
    {'id': 2 , "name":"Elen"},
    {'id': 3 , "name":"Póó"}

]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context )

def room(request, pk):
    return render(request, "base/room.html")