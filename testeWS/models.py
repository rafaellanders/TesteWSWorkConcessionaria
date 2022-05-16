from django.db import models


class Marca(models.Model):
    nome_marca = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_marca


class  Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    valor_fipe = models.FloatField()

    def __str__(self):
        return self.nome


class Carro(models.Model):
    COMBUSTIVEIS = (
        ('F', 'Flex'),
        ('A', 'Alcool'),
        ('G', 'Gasolina')
    )
    PORTAS = (
        ('2', 'Duas Portas'),
        ('4', 'Quatro Portas')
    )

    timestamp_cadastro = models.DateTimeField(auto_now_add=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    marca_id = models.ForeignKey(Marca,on_delete=models.CASCADE)
    ano = models.IntegerField()
    combustivel = models.CharField(max_length=1, choices=COMBUSTIVEIS, blank=False, null=False, default='G')
    num_portas = models.CharField(max_length=1, choices=PORTAS, blank=False, null=False, default='4')
    cor = models.CharField(max_length=30)

