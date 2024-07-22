from django.db import models
from datetime import datetime
'''
* investimento
* valor
* pago
* data
'''
class Investimento(models.Model):
    invesimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)
    # nivel = models.IntegerField(default=1) #Sempre para adicionar uma Migration
    # python manage.py makemigrations - Remove!
    # python manage.py migrate limpando tabela no banco de dados
    # Sql qual foi o comando para saber qual foi o comando Sql rodado para saber python manage.py sqlmigrate invista_me 0001_initial