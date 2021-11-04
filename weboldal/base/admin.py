from django.contrib import admin

from .models import Room, Topic, Message,  Bolygo_1, BolygoJegyben_1, BolygoHazban_1, Jegy_1, HazJegyben_1, Haz_1

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)


admin.site.register(Bolygo_1)
admin.site.register(BolygoHazban_1)
admin.site.register(BolygoJegyben_1)
admin.site.register(Jegy_1)
admin.site.register(HazJegyben_1)
admin.site.register(Haz_1)
