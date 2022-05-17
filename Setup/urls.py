from rest_framework.routers import DefaultRouter
from testeWS.views import MarcasViewset, ModeloViewset, CarroViewset, ListaCarros
from django.contrib import admin
from django.urls import path, include


router = DefaultRouter()
router.register('marcas',MarcasViewset, basename='Marcas')
router.register('modelos',ModeloViewset, basename='Modelos')
router.register('carros',CarroViewset, basename='Carros')


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('lista/',ListaCarros.as_view())

]

