import datetime

from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    # topic, ha ez a valtozo nullra áll akkor a databaseban is nulra kell allitani ezt (mind2 helyen ugyanannak kell lennie)

    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    discription = models.TextField(null=True, blank=True)  # null - can be blank
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)  # tobbszor is lefut
    created = models.DateTimeField(auto_now_add=True)  # ez csak egyszer fut le amikor belepsz eloszor a zsobaba

    class Meta:
        ordering = ['-updated', "-created"]

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)  # one to many relationshiy, one user can have multiple messages
    # ondelete==> ha valaki kitörli a szobát mit szeretnénk tenni az üzenetekkel benne? - casade - minden torlodika ami a szobaban volt
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # many to one relationship
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)  # tobbszor is lefut
    created = models.DateTimeField(auto_now_add=True)  # ez csak egyszer fut le amikor belepsz eloszor a zsobaba
    created2 = models.DateTimeField(auto_now_add=True)  # ez csak egyszer fut le amikor belepsz eloszor a zsobaba

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]  # az elso 50 karakteret jelenitjuk meg az uzenetnek


class Analogia(models.Model):
    nevID = models.CharField(max_length=30, unique=True)
    leiras = models.TextField(max_length=30, blank=True)

    class Meta:
        abstract = True


class OsszetettAnalogia(models.Model):
    leiras = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class Jegy(Analogia):
    elem = models.CharField(max_length=20, blank=True)
    minoseg = models.CharField(max_length=20, blank=True)
    paritas = models.CharField(max_length=20, blank=True)
    evszak = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nevID


class Bolygo(Analogia):
    tipus = models.CharField(max_length=40, blank=True)
    pontertek = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.nevID


class Haz(Analogia):
    tipus = models.CharField(max_length=50, blank=True)
    mundan_jegye = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.nevID)


class BolygoJegyben2(OsszetettAnalogia):
    bolygo = models.ForeignKey(Bolygo, on_delete=models.CASCADE)
    jegy = models.ForeignKey(Jegy, on_delete=models.CASCADE)

    # ferfi = models.TextField(max_length=200, blank=True, null=True)  # nap(ferfi) hold(no_pár) venusz mars
    # no = models.TextField(max_length=200, blank=True, null=True)  # nap() hold(anya, feleseg) venusz mars
    # gyerek = models.TextField(max_length=200, blank=True, null=True)  # nap hold merkur
    # szulo = models.TextField(max_length=200, blank=True, null=True)  # nap(apa
    #
    # hold_erzelmek = models.TextField(max_length=200, blank=True, null=True)
    # hold_tehetseg = models.TextField(max_length=200, blank=True, null=True)
    # hold_alarendeltseg = models.TextField(max_length=200, blank=True, null=True)
    # hold_befogadas = models.TextField(max_length=200, blank=True, null=True)
    #
    # # merkur
    # merk_gondolkodas = models.TextField(max_length=200, blank=True, null=True)
    # merk_kapcsolatteremtes = models.TextField(max_length=200, blank=True, null=True)
    # merk_kommunkacio = models.TextField(max_length=200, blank=True, null=True)
    # mozgekonysag_valtoztatas = models.TextField(max_length=200, blank=True, null=True)
    # gyermekkora = models.TextField(max_length=200, blank=True, null=True)
    # tanulasa = models.TextField(max_length=200, blank=True, null=True)
    # elfogadasa = models.TextField(max_length=200, blank=True, null=True)
    #
    # # venusz
    # venu_anyahoz_valo_viszony = models.TextField(max_length=200, blank=True, null=True)
    # venu_biztonsagvagy = models.TextField(max_length=200, blank=True, null=True)
    # venu_stabilitas_igeny = models.TextField(max_length=200, blank=True, null=True)
    # venu_szepseghez_valo_viszony = models.TextField(max_length=200, blank=True, null=True)
    # venu_noiesseg = models.TextField(max_length=200, blank=True, null=True)
    # venu_szexualitas = models.TextField(max_length=200, blank=True, null=True)
    # venu_muveszet = models.TextField(max_length=200, blank=True, null=True)
    # venu_onelfogadas = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.jegy) + "-" + str(self.bolygo)


class HazJegyben(OsszetettAnalogia):
    haz = models.ForeignKey(Haz, on_delete=models.CASCADE)
    jegy = models.ForeignKey(Jegy, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.haz) + "-" + str(self.jegy)


class BolygoHazban(OsszetettAnalogia):
    bolygo = models.ForeignKey(Bolygo, on_delete=models.CASCADE)
    haz = models.ForeignKey(Haz, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.bolygo) + "-" + str(self.haz)


#
#
# class KonkretBolygoJegyben4(models.Model):
#     bolygojegybenKULCS = models.ForeignKey(BolygoJegyben4, on_delete=models.CASCADE)
#     datumido = models.DateTimeField()
#
#
# class KonkretHazJegyben4(models.Model):
#
#     @classmethod
#     def create(cls, name):
#         return cls(name=name)
#
#     bolygohazbanKULCS = models.ForeignKey(BolygoHazban4, on_delete=models.CASCADE)


class Horoszkop1(models.Model):
    tulajdonos_neve = models.CharField(max_length=30)
    idopont = models.DateTimeField(default=datetime.datetime.now())
    hely = models.CharField(max_length=80, blank=True)
    tipus = models.CharField(max_length=30, blank=True)

    nap = models.ForeignKey(BolygoJegyben2, related_name='nap+', on_delete=models.CASCADE)
    hold = models.ForeignKey(BolygoJegyben2, related_name='hold+', on_delete=models.CASCADE)
    merkur = models.ForeignKey(BolygoJegyben2, related_name='merkur+', on_delete=models.CASCADE)
    venusz = models.ForeignKey(BolygoJegyben2, related_name='venusz+', on_delete=models.CASCADE)
    mars = models.ForeignKey(BolygoJegyben2, related_name='mars+', on_delete=models.CASCADE)
    jupiter = models.ForeignKey(BolygoJegyben2, related_name='jupiter+', on_delete=models.CASCADE)
    szaturnusz = models.ForeignKey(BolygoJegyben2, related_name='szaturnusz+', on_delete=models.CASCADE)
    uranusz = models.ForeignKey(BolygoJegyben2, related_name='uranusz+', on_delete=models.CASCADE)
    neptun = models.ForeignKey(BolygoJegyben2, related_name='neptun+', on_delete=models.CASCADE)
    pluto = models.ForeignKey(BolygoJegyben2, related_name='pluto+', on_delete=models.CASCADE)

    haz_1 = models.ForeignKey(HazJegyben, related_name='1+', on_delete=models.CASCADE)
    haz_2 = models.ForeignKey(HazJegyben, related_name='2+', on_delete=models.CASCADE)
    haz_3 = models.ForeignKey(HazJegyben, related_name='3+', on_delete=models.CASCADE)
    haz_4 = models.ForeignKey(HazJegyben, related_name='4+', on_delete=models.CASCADE)
    haz_5 = models.ForeignKey(HazJegyben, related_name='5+', on_delete=models.CASCADE)
    haz_6 = models.ForeignKey(HazJegyben, related_name='6+', on_delete=models.CASCADE)
    haz_7 = models.ForeignKey(HazJegyben, related_name='7+', on_delete=models.CASCADE)
    haz_8 = models.ForeignKey(HazJegyben, related_name='8+', on_delete=models.CASCADE)
    haz_9 = models.ForeignKey(HazJegyben, related_name='9+', on_delete=models.CASCADE)
    haz_10 = models.ForeignKey(HazJegyben, related_name='10+', on_delete=models.CASCADE)
    haz_11 = models.ForeignKey(HazJegyben, related_name='11+', on_delete=models.CASCADE)
    haz_12 = models.ForeignKey(HazJegyben, related_name='12+', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tulajdonos_neve) + "-" + str(self.tipus)
