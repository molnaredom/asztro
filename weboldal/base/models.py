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
    discription = models.TextField(null=True, blank=True)# null - can be blank
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)# tobbszor is lefut
    created = models.DateTimeField(auto_now_add=True) # ez csak egyszer fut le amikor belepsz eloszor a zsobaba

    class Meta:
        ordering = ['-updated', "-created"]

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # one to many relationshiy, one user can have multiple messages
    # ondelete==> ha valaki kitörli a szobát mit szeretnénk tenni az üzenetekkel benne? - casade - minden torlodika ami a szobaban volt
    room = models.ForeignKey(Room, on_delete=models.CASCADE)# many to one relationship
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)  # tobbszor is lefut
    created = models.DateTimeField(auto_now_add=True)  # ez csak egyszer fut le amikor belepsz eloszor a zsobaba

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50] # az elso 50 karakteret jelenitjuk meg az uzenetnek







class Analogia(models.Model):
    nevID = models.CharField(max_length=30)
    leiras = models.TextField(null=True, blank=True)

    class Meta:
        abstract= True

class OsszetettAnalogia(models.Model):
    osszetett_nevID = models.CharField(max_length=30)

    class Meta:
        abstract= True


class Jegy(Analogia):
    elem = models.CharField(max_length=6)
    minoseg = models.CharField(max_length=10)
    dekadjegy = models.CharField(max_length=8)
    paritas = models.CharField(max_length=7)
    evszak = models.CharField(max_length=6)

    def __str__(self):
        return self.nevID


class Bolygo(Analogia):
    tipusa = models.CharField(max_length=20)
    pontertek = models.IntegerField()
    jegyfokszam = models.FloatField()
    oszfokszam = models.FloatField()

    def __str__(self):
        return self.nevID


class Haz(Analogia):
    haztipus = models.CharField(max_length=20)
    jegyfokszam = models.FloatField(blank=True)
    oszfokszam = models.FloatField( blank=True)

    ura = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.nevID)


class BolygoJegyben(OsszetettAnalogia):
    bolygo = models.ForeignKey(Bolygo, on_delete=models.CASCADE)
    jegy = models.ForeignKey(Jegy, on_delete=models.CASCADE)


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

    # def __str__(self):
    #     return str(self.jegy) + "-" + str(self.bolygo)


class HazJegyben(OsszetettAnalogia):
    haz = models.ForeignKey(Haz, on_delete=models.CASCADE)
    jegy = models.ForeignKey(Jegy, on_delete=models.CASCADE)

    tulajdonsagok = models.JSONField(blank=True)

    # def __str__(self):
    #     return str(self.jegyid) + "-" + str(self.hazid)


class BolygoHazban(OsszetettAnalogia):
    bolygo = models.ForeignKey(Bolygo, on_delete=models.CASCADE)
    haz = models.ForeignKey(Haz, on_delete=models.CASCADE)

    tulajdonsagok = models.JSONField(blank=True)





    # def __str__(self):
    #     return str(self.hazid) + "-" + str(self.bolygoid)
