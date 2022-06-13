from django.db import models


class Tunet(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Bolygoszimbolum():
    bolygo = models.CharField(max_length=200)

    def __str__(self):
        return self.bolygo


class Bolygoszimbolumcsoport(models.Model):
    bolygokompozicio = models.CharField(max_length=200)
    hozzatartozo_tunet = models.ManyToManyField(Tunet, on_delete=models.CASCADE)

    def __str__(self):
        return self.bolygokompozicio


class Jelentes(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

