import random

from django.shortcuts import render
from django.db.models import Count, Max
from ..models import Jegy2, Bolygo2, Haz2, BolygoHazban2, BolygoJegyben2, HazJegyben2, Horoszkop2, HazUraHazban
from ..default_parameters import *



# több oldalt tartalmazo,analógiatároló felület
def jegyek_oldal(request):
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
    printd("hejj", bolygok,problema="bolygok_oldal")
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

    jegyek = BolygoJegyben2.objects.all()
    context = {'adatok': jegyek, "jegy_alapjan_lekeres": jegy_alapjan_lekeres}
    return render(request, 'analogiatarolok/bolygokJegyekben.html', context)


def bolygokHazakban(request):
    bolygokhazban = BolygoHazban2.objects.all()

    context = {'adatok': bolygokhazban}
    return render(request, 'analogiatarolok/bolygokHazakban.html', context)


def hazakJegyekben(request):
    hazjegyben = HazJegyben2.objects.all()
    context = {'adatok': hazjegyben}
    return render(request, 'analogiatarolok/hazakJegyekben.html', context)


def hazakUraHazakban(request):
    hazUraHazban = HazUraHazban.objects.all()
    context = {'adatok': hazUraHazban}
    return render(request, 'analogiatarolok/hazakUraHazakban.html', context)


def horoszkop_gyujtemeny(request):
    fgv_nev = "horoszkop_gyujtemeny"
    bolygo_es_jegy_lekerdezes, haz_es_jegy_lekerdezes, leker_1, leker_2, leker_3 = {}, {}, {}, {}, {}

    if request.method == "POST":

        if 'bolygo_es_jegy_lekerdezes' in request.POST:
            jegyNev = request.POST.get('jegyNev')
            bolygoNev = request.POST.get('bolygoNev')
            bolygo_es_jegy_lekerdezes = bolygo_alapjan_lekeres(bolygoNev, jegyNev)


        elif "haz_es_jegy_lekerdezes" in request.POST:
            jegyNev = request.POST.get('jegyNev')
            hazNev = request.POST.get('hazNev')
            haz_es_jegy_lekerdezes = haz_alapjan_lekeres(hazNev, jegyNev)

        # elif "leker_1" in request.POST:
        #     leker_1 = Horoszkop1.objects.filter(jupiter__jegy__elem="levegő")
        #
        # elif "leker_2" in request.POST:
        #
        #     leker_2 = Horoszkop1.objects.raw("""
        #     select *, COUNT(tulajdonos_neve) as evszak_szam
        #     from base_horoszkop1
        #     inner join base_bolygojegyben bj on base_horoszkop1.nap_id = bj.id
        #     inner join  base_jegy jegy on bj.jegy_id = jegy.id
        #     group by jegy.evszak""")
        #
        # elif "leker_3" in request.POST:
        #
        #     leker_3 = Horoszkop1.objects.raw("""
        #     select *,haz.tipus as haztipus, COUNT(tulajdonos_neve) as haztipus_szam
        #     from base_horoszkop1
        #     inner join base_hazjegyben as hj on base_horoszkop1.haz_1_id = hj.id
        #     inner join  base_haz as haz on hj.id = haz.id
        #     inner join base_bolygojegyben bj on base_horoszkop1.hold_id = bj.id
        #     where bj.leiras = ''
        #     group by haz.tipus
        #
        #                                        """)

    def nevet_privatra(nev):
        nev = str(nev)
        if len(nev.split()) == 1:
            return nev[0] + (len(nev.split()[0])-1) * "*"
        elif len(nev.split()) >= 1:
            return nev[0] + (len(nev.split()[0])-1) * "*"+ " " + len(nev.split()[1]) * "*"

    hpok = Horoszkop2.objects.all()

    context = {}
    if request.user.is_superuser:
        printd("superuser",problema=fgv_nev)
        context = {'adatok': hpok,
               "bolygo_es_jegy_lekerdezes": bolygo_es_jegy_lekerdezes,
               "haz_es_jegy_lekerdezes": haz_es_jegy_lekerdezes,
               "leker_1": leker_1,
               "leker_2": leker_2,
               "leker_3": leker_3
                }
    else:
        for horoszkop in hpok:
            horoszkop.tulajdonos_neve = nevet_privatra(horoszkop.tulajdonos_neve)
        context = {'adatok': hpok,
                   "bolygo_es_jegy_lekerdezes": bolygo_es_jegy_lekerdezes,
                   "haz_es_jegy_lekerdezes": haz_es_jegy_lekerdezes,
                   "leker_1": leker_1,
                   "leker_2": leker_2,
                   "leker_3": leker_3
                   }

    return render(request, 'analogiatarolok/horoszkop_gyujtemeny.html', context)


def bolygo_alapjan_lekeres(bolygoNev, jegyNev):
    fgv_nev = "bolygo_alapjan_lekeres"
    printd(Horoszkop2.objects.filter(nap__jegy__nevID=jegyNev).query, problema=fgv_nev)
    jegy_alapjan_lekeres = None
    if bolygoNev == "nap":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(nap__jegy__nevID=jegyNev)
    elif bolygoNev == "hold":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(hold__jegy__nevID=jegyNev)
    elif bolygoNev == "merkur":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(merkur__jegy__nevID=jegyNev)
    elif bolygoNev == "mars":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(mars__jegy__nevID=jegyNev)
    elif bolygoNev == "vénusz":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(venusz__jegy__nevID=jegyNev)
    elif bolygoNev == "jupiter":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(jupiter__jegy__nevID=jegyNev)
    elif bolygoNev == "szaturnusz":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(szaturnusz__jegy__nevID=jegyNev)
    elif bolygoNev == "uránusz":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(uranusz__jegy__nevID=jegyNev)
    elif bolygoNev == "neptun":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(neptun__jegy__nevID=jegyNev)
    elif bolygoNev == "plúto":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(pluto__jegy__nevID=jegyNev)
    return jegy_alapjan_lekeres


def haz_alapjan_lekeres(hazNev, jegyNev):
    jegy_alapjan_lekeres = None
    if hazNev == "1":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(haz_1__jegy__nevID=jegyNev)
    elif hazNev == "2":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(haz_2__jegy__nevID=jegyNev)
    elif hazNev == "3":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(haz_3__jegy__nevID=jegyNev)
    elif hazNev == "4":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(haz_4__jegy__nevID=jegyNev)
    elif hazNev == "5":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(haz_5__jegy__nevID=jegyNev)
    elif hazNev == "6":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(haz_6__jegy__nevID=jegyNev)
    elif hazNev == "7":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(haz_7__jegy__nevID=jegyNev)
    elif hazNev == "8":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(haz_8__jegy__nevID=jegyNev)
    elif hazNev == "9":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(haz_9__jegy__nevID=jegyNev)
    elif hazNev == "10":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(haz_10__jegy__nevID=jegyNev)
    elif hazNev == "11":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(haz_11__jegy__nevID=jegyNev)
    elif hazNev == "12":
        jegy_alapjan_lekeres = Horoszkop2.objects.filter(haz_12__jegy__nevID=jegyNev)
    return jegy_alapjan_lekeres