from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Shows, Reservations
from .serializers import ShowsSerializer, ReservationsSerializer
from .permissions import IsAdminOrReadOnly

class ShowsViewSet(viewsets.ModelViewSet):
    queryset = Shows.objects.all().order_by("id")
    serializer_class = ShowsSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["price", "available_seats", "movie_title"]
    ordering_fields = ["id", "movie_title", "room"]
    
class ReservationsViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.select_related("marca").all().order_by("-id")
    serializer_class = VehiculoSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["marca"]
    search_fields = ["modelo", "placa", "color", "marca__nombre"]
    ordering_fields = ["id", "anio", "modelo", "placa", "creado_en"]