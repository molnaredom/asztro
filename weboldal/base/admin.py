from django.contrib import admin

from .models import Room, Topic, Message, Analogiaa, Bolygo, BolygoJegyben, BolygoHazban, Jegy, HazJegyben, Haz

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Analogiaa)


admin.site.register(Bolygo)
admin.site.register(BolygoHazban)
admin.site.register(BolygoJegyben)
admin.site.register(Jegy)
admin.site.register(HazJegyben)
admin.site.register(Haz)
