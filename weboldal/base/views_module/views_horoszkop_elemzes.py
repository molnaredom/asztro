from django.shortcuts import render

from ..horoszkop_elemzes.horoszkopelemzo_manager import _elemzes
from ..horoszkop_elemzes.kisegito import nevet_privatra
from ..models import Horoszkop2, Jegy2, HazUraHazban


def horoszkop(request, id):
    analogia = Horoszkop2.objects.get(id=id)
    hazakUraHazakban = HazUraHazban.objects.all()
    osszesjegy = Jegy2.objects.all()
    if request.user.is_superuser:
        analogia.tulajdonos_neve = nevet_privatra(analogia.tulajdonos_neve)

    # print(analogia.fokszamok)
    if "analogiak" not in analogia.fokszamok:
        analogia.fokszamok = eval(dict(analogia.fokszamok)["analogiak"])  # eval strbol dictet csinal
    else:
        analogia.fokszamok = analogia.fokszamok["analogiak"]

    elemzes_adat = _elemzes(analogia, osszesjegy, hazakUraHazakban)
    context = {"analogia": analogia, "elemzes": elemzes_adat}  # ez egy objektum

    return render(request, "konkret_analogiak/horoszkop.html", context)


