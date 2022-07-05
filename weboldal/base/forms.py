from django.forms import ModelForm
from django import forms
from .models import Room2, Jegy2, Haz2, Bolygo2, BolygoJegyben2, HazJegyben2, BolygoHazban2, Horoszkop2, HazUraHazban, \
    HoroszkopAdatok, Munkatipus
from django.forms import formset_factory, modelformset_factory


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
        # fields = "__all__"
        fields = ["tulajdonos_neve", "idopont","pontossag", "hely", "neme", "leirasok"]
        widgets = {
            "tulajdonos_neve": forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Pl.: Kis Miklós"}),
            "hely": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Pl.: Győr"}),
            "idopont" : forms.DateTimeInput(attrs={'class': 'form-control'}),
            "neme" : forms.Select(attrs={'class': 'form-control'}),
            "pontossag" : forms.Select(attrs={'class': 'form-control'}),
            "leirasok" : forms.Textarea(attrs={'class': 'form-control'})
        }


class HoroszkopFormGyorsPontositas(ModelForm):
    class Meta:
        model = Horoszkop2
        fields = ["tulajdonos_neve", "idopont","pontossag", "hely", "neme"]
        widgets = {
            "tulajdonos_neve": forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Pl.: Kis Miklós"}),
            "hely": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Pl.: Győr"}),
            "idopont" : forms.DateTimeInput(attrs={'class': 'form-control'} ),
            "neme" : forms.Select(attrs={'class': 'form-control'}),
            "pontossag" : forms.Select(attrs={'class': 'form-control'})
        }


class MunkatipusForm(forms.Form):
    munkanev = forms.CharField(
        label='Munka',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Add meg egy munkád'
        })
    )


MunkatipusFormset = formset_factory(MunkatipusForm, extra=1)


MunkatipusModelFormset = modelformset_factory(
    Munkatipus,
    fields=('munkanev', ),
    extra=1,
    widgets={'munkanev': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Munkanév'
        })
    }
)


class HoroszkopFormAutomatic(ModelForm):
    class Meta:
        model = Horoszkop2
        # fields = "__all__"
        fields = []


class HoroszkopAdatokForm(ModelForm):
    class Meta:
        model = HoroszkopAdatok
        fields = "__all__"


class HazUraHazbanForm(ModelForm):
    class Meta:
        model = HazUraHazban
        fields = "__all__"


from django import forms
from .models import Quiz, Question, Answer


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('name', 'desc', 'number_of_questions', 'time')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('content', 'quiz')


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("content", 'question', 'correct')
