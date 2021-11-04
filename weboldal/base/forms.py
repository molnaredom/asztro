from django.forms import ModelForm
from .models import Room, Jegy_1, Haz_1, Bolygo_1, BolygoJegyben_1, HazJegyben_1, BolygoHazban_1

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ["host", "participants"]

class AnalogiaForm(ModelForm):
    class Meta:
        model = Jegy_1
        fields = "__all__"


class JegyekForm(ModelForm):
    class Meta:
        model = Jegy_1
        fields = "__all__"


class HazakForm(ModelForm):
    class Meta:
        model = Haz_1
        fields = "__all__"


class BolygokForm(ModelForm):
    class Meta:
        model = Bolygo_1
        fields = "__all__"


class BolygoJegybenForm(ModelForm):
    class Meta:
        model = BolygoJegyben_1
        fields = "__all__"


class BolygoHazbanForm(ModelForm):
    class Meta:
        model = BolygoHazban_1
        fields = "__all__"


class HazJegybenForm(ModelForm):
    class Meta:
        model = HazJegyben_1
        fields = "__all__"

