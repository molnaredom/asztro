from django.forms import ModelForm
from .models import Room4, Jegy4, Haz4, Bolygo4, BolygoJegyben4, HazJegyben4, BolygoHazban4, Horoszkop4

class RoomForm(ModelForm):
    class Meta:
        model = Room4
        fields = "__all__"
        exclude = ["host", "participants"]

class AnalogiaForm(ModelForm):
    class Meta:
        model = Jegy4
        fields = "__all__"


class JegyekForm(ModelForm):
    class Meta:
        model = Jegy4
        fields = "__all__"


class HazakForm(ModelForm):
    class Meta:
        model = Haz4
        fields = "__all__"


class BolygokForm(ModelForm):
    class Meta:
        model = Bolygo4
        fields = "__all__"


class BolygoJegybenForm(ModelForm):
    class Meta:
        model = BolygoJegyben4
        fields = "__all__"


class BolygoHazbanForm(ModelForm):
    class Meta:
        model = BolygoHazban4
        fields = "__all__"


class HazJegybenForm(ModelForm):
    class Meta:
        model = HazJegyben4
        fields = "__all__"


class HoroszkopForm(ModelForm):
    class Meta:
        model = Horoszkop4
        fields = "__all__"

