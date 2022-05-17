from django.db import models
from django_unixdatetimefield import UnixDateTimeField



class Marca(models.Model):
    nome_marca = models.CharField(max_length=100)
    # habilitando o método especial '__str__' para que o operador consiga ver a instancia em formato string.
    def __str__(self):
        return self.nome_marca


class  Modelo(models.Model):

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    valor_fipe = models.FloatField()

    def __str__(self):
        return self.nome


class Carro(models.Model):
    COMBUSTIVEIS = (   #permitindo que o operador escolha dentre as opções delimitadas
        ('F', 'Flex'),
        ('A', 'Alcool'),
        ('G', 'Gasolina')
    )
    PORTAS = (
        ('2', 'Duas Portas'),
        ('4', 'Quatro Portas')
    )

    timestamp_cadastro = models.DateTimeField(auto_now_add=True) # modelo datetime provido pelo Django. Não foi possivel deixar em modelo Unix
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    marca_id = models.ForeignKey(Marca,on_delete=models.CASCADE) #comando para chamar chaves estrangeiras
    ano = models.IntegerField() # ano sempre em inteiros
    combustivel = models.CharField(max_length=1, choices=COMBUSTIVEIS, blank=False, null=False, default='G') #habilitando a escolha
    num_portas = models.CharField(max_length=1, choices=PORTAS, blank=False, null=False, default='4')
    cor = models.CharField(max_length=30)