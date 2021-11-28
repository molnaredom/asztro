from django.contrib import admin

from .models import Room, Topic, Message,  Bolygo, BolygoJegyben2, BolygoHazban, Jegy, HazJegyben, Haz, \
        Horoszkop1

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)


admin.site.register(Bolygo)
admin.site.register(BolygoHazban)
admin.site.register(BolygoJegyben2)
admin.site.register(Jegy)
admin.site.register(HazJegyben)
admin.site.register(Haz)
admin.site.register(Horoszkop1)
