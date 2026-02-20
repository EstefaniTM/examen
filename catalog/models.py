from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Shows(models.Model):
    shows = models.ForeignKey(Shows, on_delete=models.PROTECT, related_name="boletos")
    movie_title = models.CharField(max_length=120)
    room  = models.CharField(max_length=20)
    price = models.IntegerField(
        null=True, blank=True
    )
    available_seats = models.DecimalField(
        max_digits=10,  # total de dígitos
        decimal_places=2,  # decimales
        default=0
    )
    def __str__(self):
        return f"{self.shows.nombre} {self.movie_title} ({self.room})"
    
class reservations (models.Model):
    nombre = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.nombre
