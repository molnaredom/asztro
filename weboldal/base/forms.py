from django.forms import ModelForm
from .models import Room, Analogiaa

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"

class AnalogiaForm(ModelForm):
    class Meta:
        model = Analogiaa
        fields = "__all__"
