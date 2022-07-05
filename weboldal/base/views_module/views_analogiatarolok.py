from django.shortcuts import render
from ..models import Jegy2, Bolygo2, Haz2, BolygoHazban2, BolygoJegyben2, HazJegyben2, Horoszkop2, HazUraHazban
from ..kisegito import kisegito


def jegyek_oldal(request):
    """
    több oldalt tartalmazo, analógiatároló felület
    """
    jegyek = Jegy2.objects.all()
    # jegy_minoseg_lekerdezes = {}
    # if request.method == "POST":
    #     minoseg_neve = request.POST.get('minoseg')
    #     jegy_minoseg_lekerdezes = Jegy.objects.filter(minoseg=minoseg_neve)
    #
    context = {'adatok': jegyek}  # , "jegy_minoseg_lekerdezes": jegy_minoseg_lekerdezes}
    return render(request, 'analogiatarolok/jegyek.html', context)


def bolygok_oldal(request):
    bolygok = Bolygo2.objects.all()
    bolygotipus_lekerdezes = {}
    if request.method == "POST":
        tipusnev = request.POST.get('bolygotipus')
        bolygotipus_lekerdezes = Bolygo2.objects.filter(tipus=tipusnev)
    context = {'adatok': bolygok, "bolygotipus_lekerdezes": bolygotipus_lekerdezes}
    return render(request, 'analogiatarolok/bolygok.html', context)


def hazak_oldal(request):
    hazak = Haz2.objects.all()
    haztipus_lekerdezes = {}
    if request.method == "POST":
        haztipus_lekerdezes = Haz2.objects.filter(tipus=request.POST.get('tipus'))

    context = {'adatok': hazak, "haztipus_lekerdezes": haztipus_lekerdezes}
    return render(request, 'analogiatarolok/hazak.html', context)


def bolygokJegyekben(request):
    jegy_alapjan_lekeres = {}
    if request.method == "POST":
        jegyNev = request.POST.get('jegyNev')
        jegy_alapjan_lekeres = BolygoJegyben2.objects.filter(jegy__nevID=jegyNev)

    context = {'adatok': BolygoJegyben2.objects.all(),
               "jegy_alapjan_lekeres": jegy_alapjan_lekeres
               }
    return render(request, 'analogiatarolok/bolygokJegyekben.html', context)


def bolygokHazakban(request):
    return render(request,
                  'analogiatarolok/bolygokHazakban.html',
                  {'adatok': BolygoHazban2.objects.all()})


def hazakJegyekben(request):
    return render(request,
                  'analogiatarolok/hazakJegyekben.html',
                  {'adatok': HazJegyben2.objects.all()})


def hazakUraHazakban(request):
    return render(request,
                  'analogiatarolok/hazakUraHazakban.html',
                  {'adatok': HazUraHazban.objects.all()})


def horoszkop_gyujtemeny(request):
    bolygo_es_jegy_lekerdezes, bolygo_es_haz_lekerdezes, haz_es_jegy_lekerdezes = {}, {}, {}
    lekerdezes_neve = None
    bolygo_nevek = ["nap", "hold", "merkúr", "vénusz", "mars", "jupiter", "szaturnusz", "uránusz", "neptun",
                    "pluto"]

    def privat_nev_ha_nem_superuser(lekerdezes, request):
        if not request.user.is_superuser:
            for horoszkop in lekerdezes:
                nev = str(horoszkop.tulajdonos_neve)
                if len(nev.split()) == 1:
                    horoszkop.tulajdonos_neve = nev[0] + (len(nev.split()[0]) - 1) * "*"
                elif len(nev.split()) >= 1:
                    horoszkop.tulajdonos_neve = nev[0] + (len(nev.split()[0]) - 1) * "*" + " " + len(
                        nev.split()[1]) * "*"

    if request.method == "POST":
        if 'bolygo_es_jegy_lekerdezes' in request.POST:
            bolygoNev = request.POST.get('bolygoNev')
            jegyNev = request.POST.get('jegyNev')

            bolygo_es_jegy_lekerdezes = bolygo_alapjan_lekeres(
                bolygoNev, jegyNev, bolygo_nevek
            )
            lekerdezes_neve = f"Jegy: {jegyNev} --  Bolgyó: {bolygoNev}"
            privat_nev_ha_nem_superuser(bolygo_es_jegy_lekerdezes, request)

        elif "haz_es_jegy_lekerdezes" in request.POST:
            hazNev = request.POST.get('hazNev')
            jegyNev = request.POST.get('jegyNev')

            haz_es_jegy_lekerdezes = haz_alapjan_lekeres(hazNev, jegyNev)
            print(haz_es_jegy_lekerdezes, ".............")

            lekerdezes_neve = f"Jegy: {jegyNev}  --  Ház: {hazNev}"
            privat_nev_ha_nem_superuser(haz_es_jegy_lekerdezes, request)

        elif "bolygo_es_haz_lekerdezes" in request.POST:
            bolygoNev = request.POST.get('bolygoNev')
            hazNev = request.POST.get('hazNev')

            bolygo_es_haz_lekerdezes = bolygo_hazban_alapjan_lekeres(bolygoNev, hazNev, bolygo_nevek)

            lekerdezes_neve = f"Ház: {hazNev} --  Bolygó: {bolygoNev}"
            privat_nev_ha_nem_superuser(bolygo_es_haz_lekerdezes, request)
            print([i for i in bolygo_es_haz_lekerdezes])

    hpok = Horoszkop2.objects.all()
    privat_nev_ha_nem_superuser(hpok, request)


    context = {'adatok': hpok,
               "bolygo_es_jegy_lekerdezes": bolygo_es_jegy_lekerdezes,
               "haz_es_jegy_lekerdezes": haz_es_jegy_lekerdezes,
               "bolygo_es_haz_lekerdezes": bolygo_es_haz_lekerdezes,
               "lekerdezes_neve": lekerdezes_neve
               }

    return render(request, 'analogiatarolok/horoszkop_gyujtemeny.html', context)


def bolygo_alapjan_lekeres(bolygoNev, jegyNev, bolygo_nevek):
    if bolygoNev == bolygo_nevek[0]:
        return Horoszkop2.objects.filter(nap__jegy__nevID=jegyNev)
    elif bolygoNev == bolygo_nevek[1]:
        return Horoszkop2.objects.filter(hold_j__jegy__nevID=jegyNev)
    elif bolygoNev == bolygo_nevek[2]:
        return Horoszkop2.objects.filter(merkur_j__jegy__nevID=jegyNev)
    elif bolygoNev == bolygo_nevek[3]:
        return Horoszkop2.objects.filter(venusz_j__jegy__nevID=jegyNev)
    elif bolygoNev == bolygo_nevek[4]:
        return Horoszkop2.objects.filter(mars_j__jegy__nevID=jegyNev)
    elif bolygoNev == bolygo_nevek[5]:
        return Horoszkop2.objects.filter(jupiter_j__jegy__nevID=jegyNev)
    elif bolygoNev == bolygo_nevek[6]:
        return Horoszkop2.objects.filter(szaturnusz_j__jegy__nevID=jegyNev)
    elif bolygoNev == bolygo_nevek[7]:
        return Horoszkop2.objects.filter(uranusz_j__jegy__nevID=jegyNev)
    elif bolygoNev == bolygo_nevek[8]:
        return Horoszkop2.objects.filter(neptun_j__jegy__nevID=jegyNev)
    elif bolygoNev == bolygo_nevek[9]:
        return Horoszkop2.objects.filter(pluto_j__jegy__nevID=jegyNev)


def bolygo_hazban_alapjan_lekeres(bolygoNev, hazNev, bolygo_nevek):
    if bolygoNev == bolygo_nevek[0]:
        return Horoszkop2.objects.filter(nap_h__haz__nevID=hazNev)
    elif bolygoNev == bolygo_nevek[1]:
        return Horoszkop2.objects.filter(hold_h__haz__nevID=hazNev)
    elif bolygoNev == bolygo_nevek[2]:
        return Horoszkop2.objects.filter(merkur_h__haz__nevID=hazNev)
    elif bolygoNev == bolygo_nevek[3]:
        return Horoszkop2.objects.filter(venusz_h__haz__nevID=hazNev)
    elif bolygoNev == bolygo_nevek[4]:
        return Horoszkop2.objects.filter(mars_h__haz__nevID=hazNev)
    elif bolygoNev == bolygo_nevek[5]:
        return Horoszkop2.objects.filter(jupiter_h__haz__nevID=hazNev)
    elif bolygoNev == bolygo_nevek[6]:
        return Horoszkop2.objects.filter(szaturnusz_h__haz__nevID=hazNev)
    elif bolygoNev == bolygo_nevek[7]:
        return Horoszkop2.objects.filter(uranusz_h__haz__nevID=hazNev)
    elif bolygoNev == bolygo_nevek[8]:
        return Horoszkop2.objects.filter(neptun_h__haz__nevID=hazNev)
    elif bolygoNev == bolygo_nevek[9]:
        return Horoszkop2.objects.filter(pluto_h__haz__nevID=hazNev)


def haz_alapjan_lekeres(hazNev, jegyNev):
    if hazNev == "1":
        return Horoszkop2.objects.filter(haz_1__jegy__nevID=jegyNev)
    elif hazNev == "2":
        return Horoszkop2.objects.filter(haz_2__jegy__nevID=jegyNev)
    elif hazNev == "3":
        return Horoszkop2.objects.filter(haz_3__jegy__nevID=jegyNev)
    elif hazNev == "4":
        return Horoszkop2.objects.filter(haz_4__jegy__nevID=jegyNev)
    elif hazNev == "5":
        return Horoszkop2.objects.filter(haz_5__jegy__nevID=jegyNev)
    elif hazNev == "6":
        return Horoszkop2.objects.filter(haz_6__jegy__nevID=jegyNev)
    elif hazNev == "7":
        return Horoszkop2.objects.filter(haz_7__jegy__nevID=jegyNev)
    elif hazNev == "8":
        return Horoszkop2.objects.filter(haz_8__jegy__nevID=jegyNev)
    elif hazNev == "9":
        return Horoszkop2.objects.filter(haz_9__jegy__nevID=jegyNev)
    elif hazNev == "10":
        return Horoszkop2.objects.filter(haz_10__jegy__nevID=jegyNev)
    elif hazNev == "11":
        return Horoszkop2.objects.filter(haz_11__jegy__nevID=jegyNev)
    elif hazNev == "12":
        return Horoszkop2.objects.filter(haz_12__jegy__nevID=jegyNev)
    else:
        raise Error
