from django.contrib import admin

from .models import Room2, Topic2, Message2, Bolygo2, BolygoJegyben2, BolygoHazban2, Jegy2, HazJegyben2, Haz2, \
        Horoszkop2, HazUraHazban

admin.site.register(Room2)
admin.site.register(Topic2)
admin.site.register(Message2)


admin.site.register(Bolygo2)
admin.site.register(BolygoHazban2)
admin.site.register(BolygoJegyben2)
admin.site.register(Jegy2)
admin.site.register(HazJegyben2)
admin.site.register(Haz2)
admin.site.register(Horoszkop2)
admin.site.register(HazUraHazban)
