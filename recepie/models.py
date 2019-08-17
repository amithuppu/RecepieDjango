from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __unicode__(self):
        return self.name


class Step(models.Model):
    step_text = models.CharField(max_length=200, blank=True)
    recepie = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

class Ingredient(models.Model):
    text = models.CharField(max_length=250)
    recepie = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name




# Create your models here.
