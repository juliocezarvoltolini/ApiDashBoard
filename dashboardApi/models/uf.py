from django.db import models

from .pais import Pais


class UF(models.Model):
    id = models.BigIntegerField(primary_key=True, auto_created=False)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, unique=True, null=True)
    sigla = models.CharField(max_length=2, unique=True, null=True)
    estado = models.CharField(max_length=30, default='')
    
    class Meta():
        db_table = 'uf';
    