from django.contrib import admin

from .models import Room4, Topic4, Message4,  Bolygo4, BolygoJegyben4, BolygoHazban4, Jegy4, HazJegyben4, Haz4, \
        Horoszkop4

admin.site.register(Room4)
admin.site.register(Topic4)
admin.site.register(Message4)


admin.site.register(Bolygo4)
admin.site.register(BolygoHazban4)
admin.site.register(BolygoJegyben4)
admin.site.register(Jegy4)
admin.site.register(HazJegyben4)
admin.site.register(Haz4)
admin.site.register(Horoszkop4)
