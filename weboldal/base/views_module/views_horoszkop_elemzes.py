from django.shortcuts import render

from ..horoszkop_elemzes.horoszkopelemzo_manager import _elemzes
from ..horoszkop_elemzes.kisegito import nevet_privatra
from ..models import Horoszkop2, Jegy2, HazUraHazban


def horoszkop(request, id):
    horoszkop_obj = Horoszkop2.objects.get(id=id)
    hazakUraHazakban = HazUraHazban.objects.all()
    osszesjegy = Jegy2.objects.all()
    horoszkop_obj.munka = horoszkop_obj.munka["munkak"]

    if not request.user.is_superuser:
        horoszkop_obj.tulajdonos_neve = nevet_privatra(horoszkop_obj.tulajdonos_neve)

    for i in hazakUraHazakban:
        i.tulajdonsagok = i.tulajdonsagok["analogiak"][2:-2].split("', '")

    elemzes_adat = _elemzes(horoszkop_obj, osszesjegy, hazakUraHazakban)
    context = {"analogia": horoszkop_obj, "elemzes": elemzes_adat}  # ez egy objektum

    return render(request, "konkret_analogiak/horoszkop.html", context)


