from django.forms import ModelForm
from django import  forms
from .models import Room2, Jegy2, Haz2, Bolygo2, BolygoJegyben2, HazJegyben2, BolygoHazban2, Horoszkop2, HazUraHazban, \
    HoroszkopAdatok


class RoomForm(ModelForm):
    class Meta:
        model = Room2
        fields = "__all__"
        exclude = ["host", "participants"]


class AnalogiaForm(ModelForm):
    class Meta:
        model = Jegy2
        fields = "__all__"


class JegyekForm(ModelForm):
    class Meta:
        model = Jegy2
        fields = "__all__"


class HazakForm(ModelForm):
    class Meta:
        model = Haz2
        fields = "__all__"


class BolygokForm(ModelForm):
    class Meta:
        model = Bolygo2
        fields = "__all__"


class BolygoJegybenForm(ModelForm):
    class Meta:
        model = BolygoJegyben2
        fields = "__all__"


class BolygoHazbanForm(ModelForm):
    class Meta:
        model = BolygoHazban2
        fields = "__all__"


class HazJegybenForm(ModelForm):
    class Meta:
        model = HazJegyben2
        fields = "__all__"


class HoroszkopForm(ModelForm):
    class Meta:
        model = Horoszkop2
        fields = "__all__"


class HoroszkopFormGyors(ModelForm):
    class Meta:
        model = Horoszkop2
        fields = "__all__"


class HoroszkopAdatokForm(ModelForm):
    class Meta:
        model = HoroszkopAdatok
        fields = "__all__"


class HazUraHazbanForm(ModelForm):
    class Meta:
        model = HazUraHazban
        fields = "__all__"


class Horoszkop_Csillagjegyszures(ModelForm):
    class Meta:
        model = Horoszkop2
        fields = ["nap"]
