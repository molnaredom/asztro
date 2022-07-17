from django.shortcuts import render

from .horoscope_creator import createHoroszkopSolar
from ..horoszkop_elemzes.kisegito import nevet_privatra
from ..models import Horoszkop2, Jegy2, HazUraHazban


def horoszkop(request, id):
    horoszkop_obj = Horoszkop2.objects.get(id=id)
    # hazakUraHazakban = HazUraHazban.objects.all()
    # osszesjegy = Jegy2.objects.all()
    horoszkop_obj.munka = horoszkop_obj.munka["munkak"]

    if not request.user.is_superuser:
        horoszkop_obj.tulajdonos_neve = nevet_privatra(horoszkop_obj.tulajdonos_neve)


    # elemzes_adat = elemzes(horoszkop_obj, osszesjegy, hazakUraHazakban)
    context = {"analogia": horoszkop_obj, "elemzes": horoszkop_obj.elemzes_adat}  # ez egy objektum

    return render(request, "konkret_analogiak/horoszkop.html", context)


def szolar(request, id, ev):
    horoszkop_obj = Horoszkop2.objects.get(id=id)

    szolar_obj = createHoroszkopSolar(
        radix_hp=horoszkop_obj,
        visszateresi_ev=ev
    )

    szolar_obj.munka = szolar_obj.munka["munkak"]

    if not request.user.is_superuser:
        szolar_obj.tulajdonos_neve = nevet_privatra(szolar_obj.tulajdonos_neve)


    # elemzes_adat = elemzes(horoszkop_obj, osszesjegy, hazakUraHazakban)
    context = {"analogia": szolar_obj}  # ez egy objektum

    return render(request, "konkret_analogiak/szolarkeplet.html", context)


