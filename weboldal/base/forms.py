from django.forms import ModelForm
from .models import Room, Jegy1, Haz1, Bolygo1

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ["host", "participants"]

class AnalogiaForm(ModelForm):
    class Meta:
        model = Jegy1
        fields = "__all__"


class JegyekForm(ModelForm):
    class Meta:
        model = Jegy1
        fields = "__all__"


class HazakForm(ModelForm):
    class Meta:
        model = Haz1
        fields = "__all__"


class BolygokForm(ModelForm):
    class Meta:
        model = Bolygo1
        fields = "__all__"

