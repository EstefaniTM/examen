from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Shows(models.Model):
    
    movie_title = models.CharField(max_length=120,default="")
    room  = models.CharField(max_length=20, default="")
    price = models.IntegerField(
        null=True, blank=True, default=0
    )
    available_seats = models.DecimalField(
        max_digits=10,  # total de dígitos
        decimal_places=2,  # decimales
        default=0
    )
    def __str__(self):
        return f"{self.id} {self.movie_title} ({self.room})"

class Estado (models.TextChoices):    
    RESERVED = "reservado", "Reservado"
    CONFIRMED = "confirmado", "Confirmado"
    CANCELLED = "Cancelado", "cancelado"

  
class Reservations (models.Model):
    
    show_id = models.ForeignKey(Shows, on_delete=models.PROTECT, related_name="shows")
    customer_name = models.CharField(max_length=120)
    seats = models.IntegerField(
        null=True, blank=True, default=0
    )
    status = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.RESERVED
    )
    
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.Shows.id} {self.status} ({self.created_at})"
        
