# Generated by Django 4.0.4 on 2022-05-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testeWS', '0004_rename_marca_carro_marca_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='timestamp_cadastro',
            field=models.DateField(auto_now_add=True),
        ),
    ]