from rest_framework import serializers
from .models import Marca, Modelo, Carro


class MarcaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marca
        fields = '__all__'


class ModeloSerializer(serializers.ModelSerializer):

    class Meta:
        model = Modelo
        fields = '__all__'


class CarroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carro
        exclude=[]


class ListaCarroSerializer(serializers.ModelSerializer):

    marca_nome = serializers.ReadOnlyField(source='marca.nome_marca')
    modelo_nome = serializers.ReadOnlyField(source='modelo.nome')
    valor_fipe = serializers.ReadOnlyField(source='modelo.valor_fipe')
    class Meta:
        model = Carro
        fields = ['id','marca_id','marca_nome','modelo_nome','ano','combustivel','num_portas','valor_fipe','cor','timestamp_cada'
                                                                                                         'stro']