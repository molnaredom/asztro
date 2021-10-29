from django.contrib import admin

from .models import Room, Topic, Message,  Bolygo1, BolygoJegyben, BolygoHazban, Jegy1, HazJegyben, Haz1

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)


admin.site.register(Bolygo1)
admin.site.register(BolygoHazban)
admin.site.register(BolygoJegyben)
admin.site.register(Jegy1)
admin.site.register(HazJegyben)
admin.site.register(Haz1)
