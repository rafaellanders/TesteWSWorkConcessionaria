from rest_framework import viewsets, generics
from .models import  Marca, Modelo, Carro
from .serializers import MarcaSerializer, ModeloSerializer, CarroSerializer, ListaCarroSerializer

class MarcasViewset(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class ModeloViewset(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

class CarroViewset(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

class ListaCarros(generics.ListAPIView):
    queryset = Carro.objects.all()
    serializer_class = ListaCarroSerializer