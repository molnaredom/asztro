import datetime
import os

from django.db import models
from django.contrib.auth.models import User


class Topic2(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room2(models.Model):
    # topic, ha ez a valtozo nullra áll akkor a databaseban is nulra kell allitani ezt (mind2 helyen ugyanannak kell lennie)

    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic2, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    discription = models.TextField(null=True, blank=True)  # null - can be blank
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)  # tobbszor is lefut
    created = models.DateTimeField(auto_now_add=True)  # ez csak egyszer fut le amikor belepsz eloszor a zsobaba

    class Meta:
        ordering = ['-updated', "-created"]

    def __str__(self):
        return self.name


class Message2(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)  # one to many relationshiy, one user can have multiple messages
    # ondelete==> ha valaki kitörli a szobát mit szeretnénk tenni az üzenetekkel benne? - casade - minden torlodika ami a szobaban volt
    room = models.ForeignKey(Room2, on_delete=models.CASCADE)  # many to one relationship
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)  # tobbszor is lefut
    created = models.DateTimeField(auto_now_add=True)  # ez csak egyszer fut le amikor belepsz eloszor a zsobaba
    created2 = models.DateTimeField(auto_now_add=True)  # ez csak egyszer fut le amikor belepsz eloszor a zsobaba

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]  # az elso 50 karakteret jelenitjuk meg az uzenetnek


class Analogia2(models.Model):
    nevID = models.CharField(max_length=30, unique=True)
    leiras = models.JSONField(null=True, blank=True, default=dict)

    class Meta:
        abstract = True


class OsszetettAnalogia2(models.Model):
    leiras = models.JSONField(null=True, blank=True, default=dict)

    class Meta:
        abstract = True


class Jegy2(Analogia2):
    elem = models.CharField(max_length=20, blank=True)
    minoseg = models.CharField(max_length=20, blank=True)
    paritas = models.CharField(max_length=20, blank=True)
    evszak = models.CharField(max_length=20, blank=True)
    uralkodo_bolygo = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nevID


class Bolygo2(Analogia2):
    tipus = models.CharField(max_length=40, blank=True)
    pontertek = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.nevID


class Haz2(Analogia2):
    tipus = models.CharField(max_length=50, blank=True)
    mundan_jegye = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.nevID)


class BolygoJegyben2(OsszetettAnalogia2):
    bolygo = models.ForeignKey(Bolygo2, on_delete=models.CASCADE)
    jegy = models.ForeignKey(Jegy2, on_delete=models.CASCADE)

    adatok = models.JSONField(default= dict, blank=True)

    def __str__(self):
        return str(self.jegy) + " ◈ " + str(self.bolygo)


class HazJegyben2(OsszetettAnalogia2):
    haz = models.ForeignKey(Haz2, on_delete=models.CASCADE)
    jegy = models.ForeignKey(Jegy2, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.haz) + " ◈ " + str(self.jegy)


class BolygoHazban2(OsszetettAnalogia2):
    bolygo = models.ForeignKey(Bolygo2, on_delete=models.CASCADE)
    haz = models.ForeignKey(Haz2, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.bolygo) + " ◈ " + str(self.haz)


class HazUraHazban(models.Model):
    alap_haz = models.ForeignKey(Haz2, related_name='alap_haz', on_delete=models.CASCADE)
    ura_melyik_hazban = models.ForeignKey(Haz2, related_name='ura', on_delete=models.CASCADE)
    tulajdonsagok = models.JSONField(null=True, blank=True, default=dict)

    def __str__(self):
        return str(self.alap_haz) + ". ház ura " + str(self.ura_melyik_hazban) + ". ház"

#
# class NincsUra(OsszetettAnalogia2):
#     alap_jegy = models.ForeignKey(HazJegyben2, related_name='alap_haz', on_delete=models.CASCADE)
#     ura_melyik_hazban = models.ForeignKey(HazJegyben2, related_name='ura', on_delete=models.CASCADE)
#     talajdonasagok = models.JSONField(null=True, blank=True, default=dict)
#
#     def __str__(self):
#         return str(self.alap_haz) + ". ház ura " + str(self.ura_melyik_hazban) + ". ház"


class Horoszkop2(models.Model):
    tulajdonos_neve = models.CharField(max_length=30)
    idopont = models.DateTimeField(default=datetime.datetime.now())
    hely = models.CharField(max_length=80, blank=True)
    tipus = models.CharField(max_length=30, blank=True)

    kepletkep = models.ImageField(upload_to='blah', default= os.getcwd()+'weboldal/static/images/hold.jpg')
    leirasok = models.JSONField(default=dict, blank=True)
    fokszamok = models.JSONField(default=dict, blank=True)

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

    haz_1 = models.ForeignKey(HazJegyben2, related_name='1+', on_delete=models.CASCADE)
    haz_2 = models.ForeignKey(HazJegyben2, related_name='2+', on_delete=models.CASCADE)
    haz_3 = models.ForeignKey(HazJegyben2, related_name='3+', on_delete=models.CASCADE)
    haz_4 = models.ForeignKey(HazJegyben2, related_name='4+', on_delete=models.CASCADE)
    haz_5 = models.ForeignKey(HazJegyben2, related_name='5+', on_delete=models.CASCADE)
    haz_6 = models.ForeignKey(HazJegyben2, related_name='6+', on_delete=models.CASCADE)
    haz_7 = models.ForeignKey(HazJegyben2, related_name='7+', on_delete=models.CASCADE)
    haz_8 = models.ForeignKey(HazJegyben2, related_name='8+', on_delete=models.CASCADE)
    haz_9 = models.ForeignKey(HazJegyben2, related_name='9+', on_delete=models.CASCADE)
    haz_10 = models.ForeignKey(HazJegyben2, related_name='10+', on_delete=models.CASCADE)
    haz_11 = models.ForeignKey(HazJegyben2, related_name='11+', on_delete=models.CASCADE)
    haz_12 = models.ForeignKey(HazJegyben2, related_name='12+', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tulajdonos_neve) + " ◈ " + str(self.tipus)
