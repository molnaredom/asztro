from django.forms import ModelForm
from .models import Room, Jegy, Haz, Bolygo, BolygoJegyben, HazJegyben, BolygoHazban, Horoszkop1

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ["host", "participants"]

class AnalogiaForm(ModelForm):
    class Meta:
        model = Jegy
        fields = "__all__"


class JegyekForm(ModelForm):
    class Meta:
        model = Jegy
        fields = "__all__"


class HazakForm(ModelForm):
    class Meta:
        model = Haz
        fields = "__all__"


class BolygokForm(ModelForm):
    class Meta:
        model = Bolygo
        fields = "__all__"


class BolygoJegybenForm(ModelForm):
    class Meta:
        model = BolygoJegyben
        fields = "__all__"


class BolygoHazbanForm(ModelForm):
    class Meta:
        model = BolygoHazban
        fields = "__all__"


class HazJegybenForm(ModelForm):
    class Meta:
        model = HazJegyben
        fields = "__all__"


class HoroszkopForm(ModelForm):
    class Meta:
        model = Horoszkop1
        fields = "__all__"


class Horoszkop_Csillagjegyszures(ModelForm):
    class Meta:
        model = Horoszkop1
        fields = ["nap"]

