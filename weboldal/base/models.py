from django.db import models
from django.contrib.auth.models import User


class Topic4(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room4(models.Model):
    # topic, ha ez a valtozo nullra áll akkor a databaseban is nulra kell allitani ezt (mind2 helyen ugyanannak kell lennie)

    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic4, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    discription = models.TextField(null=True, blank=True)  # null - can be blank
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)  # tobbszor is lefut
    created = models.DateTimeField(auto_now_add=True)  # ez csak egyszer fut le amikor belepsz eloszor a zsobaba

    class Meta:
        ordering = ['-updated', "-created"]

    def __str__(self):
        return self.name


class Message4(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)  # one to many relationshiy, one user can have multiple messages
    # ondelete==> ha valaki kitörli a szobát mit szeretnénk tenni az üzenetekkel benne? - casade - minden torlodika ami a szobaban volt
    room = models.ForeignKey(Room4, on_delete=models.CASCADE)  # many to one relationship
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)  # tobbszor is lefut
    created = models.DateTimeField(auto_now_add=True)  # ez csak egyszer fut le amikor belepsz eloszor a zsobaba

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]  # az elso 50 karakteret jelenitjuk meg az uzenetnek


class Analogia4(models.Model):
    nevID = models.CharField(max_length=30)
    leiras = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class OsszetettAnalogia4(models.Model):
    osszetett_nevID = models.CharField(max_length=30)

    class Meta:
        abstract = True


class Jegy4(Analogia4):
    elem = models.CharField(max_length=6,blank=True)
    minoseg = models.CharField(max_length=10,blank=True)
    dekadjegy = models.CharField(max_length=8,blank=True)
    paritas = models.CharField(max_length=7,blank=True)
    evszak = models.CharField(max_length=6,blank=True)

    def __str__(self):
        return self.nevID

class Bolygo4(Analogia4):
    tipusa = models.CharField(max_length=20,blank=True)
    pontertek = models.IntegerField(blank=True)

    def __str__(self):
        return self.nevID


class Haz4(Analogia4):
    haztipus = models.CharField(max_length=20,blank=True)

    uralkodobolygo = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.nevID)


class BolygoJegyben4(OsszetettAnalogia4):
    bolygo = models.ForeignKey(Bolygo4, on_delete=models.CASCADE)
    jegy = models.ForeignKey(Jegy4, on_delete=models.CASCADE)

    altalanos_tul = models.CharField(max_length=300, blank=True)
    jellemzo_erosseg = models.FloatField()

    ferfi = models.CharField(max_length=200, blank=True)  # nap(ferfi) hold(no_pár) venusz mars
    no = models.CharField(max_length=200, blank=True)  # nap() hold(anya, feleseg) venusz mars
    gyerek = models.CharField(max_length=200, blank=True)  # nap hold merkur
    szulo = models.CharField(max_length=200, blank=True)  # nap(apa

    hold_erzelmek = models.CharField(max_length=200, blank=True)
    hold_tehetseg = models.CharField(max_length=200, blank=True)
    hold_alarendeltseg = models.CharField(max_length=200, blank=True)
    hold_befogadas = models.CharField(max_length=200, blank=True)

    # merkur
    merk_gondolkodas = models.CharField(max_length=200, blank=True)
    merk_kapcsolatteremtes = models.CharField(max_length=200, blank=True)
    merk_kommunkacio = models.CharField(max_length=200, blank=True)
    mozgekonysag_valtoztatas = models.CharField(max_length=200, blank=True)
    gyermekkora = models.CharField(max_length=200, blank=True)
    tanulasa = models.CharField(max_length=200, blank=True)
    elfogadasa = models.CharField(max_length=200, blank=True)

    # venusz
    venu_anyahoz_valo_viszony = models.CharField(max_length=200, blank=True)
    venu_biztonsagvagy = models.CharField(max_length=200, blank=True)
    venu_stabilitas_igeny = models.CharField(max_length=200, blank=True)
    venu_szepseghez_valo_viszony = models.CharField(max_length=200, blank=True)
    venu_noiesseg = models.CharField(max_length=200, blank=True)
    venu_szexualitas = models.CharField(max_length=200, blank=True)
    venu_muveszet = models.CharField(max_length=200, blank=True)
    venu_onelfogadas = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.jegy) + "-" + str(self.bolygo)


class HazJegyben4(OsszetettAnalogia4):
    haz = models.ForeignKey(Haz4, on_delete=models.CASCADE)
    jegy = models.ForeignKey(Jegy4, on_delete=models.CASCADE)

    tulajdonsagok = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return str(self.haz) + "-" + str(self.jegy)



class BolygoHazban4(OsszetettAnalogia4):
    bolygo = models.ForeignKey(Bolygo4, on_delete=models.CASCADE)
    haz = models.ForeignKey(Haz4, on_delete=models.CASCADE)

    tulajdonsagok = models.CharField(blank=True, max_length=200)

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


class Horoszkop4(Analogia4):
    nevID = models.CharField(max_length=30, unique=True)

    nap = models.ForeignKey(BolygoJegyben4, related_name='nap+', on_delete=models.CASCADE)
    hold = models.ForeignKey(BolygoJegyben4, related_name='hold+', on_delete=models.CASCADE)
    merkur = models.ForeignKey(BolygoJegyben4, related_name='merkur+', on_delete=models.CASCADE)
    venusz = models.ForeignKey(BolygoJegyben4, related_name='venusz+', on_delete=models.CASCADE)
    mars = models.ForeignKey(BolygoJegyben4, related_name='mars+', on_delete=models.CASCADE)
    jupiter = models.ForeignKey(BolygoJegyben4, related_name='jupiter+', on_delete=models.CASCADE)
    szaturnusz = models.ForeignKey(BolygoJegyben4, related_name='szaturnusz+', on_delete=models.CASCADE)
    uranusz = models.ForeignKey(BolygoJegyben4, related_name='uranusz+', on_delete=models.CASCADE)
    neptun = models.ForeignKey(BolygoJegyben4, related_name='neptun+', on_delete=models.CASCADE)
    pluto = models.ForeignKey(BolygoJegyben4, related_name='pluto+', on_delete=models.CASCADE)

    haz_1 = models.ForeignKey(HazJegyben4, related_name='1+', on_delete=models.CASCADE)
    haz_2 = models.ForeignKey(HazJegyben4, related_name='2+', on_delete=models.CASCADE)
    haz_3 = models.ForeignKey(HazJegyben4, related_name='3+', on_delete=models.CASCADE)
    haz_4 = models.ForeignKey(HazJegyben4, related_name='4+', on_delete=models.CASCADE)
    haz_5 = models.ForeignKey(HazJegyben4, related_name='5+', on_delete=models.CASCADE)
    haz_6 = models.ForeignKey(HazJegyben4, related_name='6+', on_delete=models.CASCADE)
    haz_7 = models.ForeignKey(HazJegyben4, related_name='7+', on_delete=models.CASCADE)
    haz_8 = models.ForeignKey(HazJegyben4, related_name='8+', on_delete=models.CASCADE)
    haz_9 = models.ForeignKey(HazJegyben4, related_name='9+', on_delete=models.CASCADE)
    haz_10 = models.ForeignKey(HazJegyben4, related_name='10+', on_delete=models.CASCADE)
    haz_11 = models.ForeignKey(HazJegyben4, related_name='11+', on_delete=models.CASCADE)
    haz_12 = models.ForeignKey(HazJegyben4, related_name='12+', on_delete=models.CASCADE)


    def __str__(self):
        return str(self.nevID) + "-" + str(self.nevID)

