from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=25)
    name_short = models.CharField(max_length=4)
    population = models.IntegerField()
    currency = models.CharField(max_length=20)

    def __str__(self):
        return self.name + "(" + self.name_short + ")"


class Player(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    d_o_b = models.DateField()
    position = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


