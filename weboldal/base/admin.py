from django.contrib import admin

from .models import *


admin.site.register(Room2)
admin.site.register(Topic2)
admin.site.register(Message2)
admin.site.register(Quiz)

admin.site.register(Munkatipus)

admin.site.register(Bolygo2)
admin.site.register(BolygoHazban2)
admin.site.register(BolygoJegyben2)
admin.site.register(Jegy2)
admin.site.register(HazJegyben2)
admin.site.register(Haz2)
admin.site.register(Horoszkop2)
admin.site.register(HazUraHazban)
admin.site.register(HoroszkopAlapadat)


class AnswerInLine(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

admin.site.register(Marks_Of_User)
