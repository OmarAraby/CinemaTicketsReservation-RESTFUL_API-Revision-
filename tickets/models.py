from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings




## Guest -- Movie -- Reservation




from django.db import models

class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=20)
    date = models.DateField()

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.movie


class Guest(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)

    class Meta: 
        verbose_name = "Guest"
        verbose_name_plural = "Guests"

    def __str__(self):
        return self.name


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, related_name='reservations', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reservations',  on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

    def __str__(self):
        return f"{self.guest} - {self.movie}"





@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenGenerate(sender , instance , created , **kwargs):
    if created :
        Token.objects.create(user=instance)
  