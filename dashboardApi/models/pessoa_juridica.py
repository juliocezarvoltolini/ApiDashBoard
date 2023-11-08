from django.db import models
from.validators import cnpj_validator


class PessoaJuridica(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    cnpj = models.CharField(max_length=14, unique=True, validators=[cnpj_validator])
    data_criacao = models.DateField(null=True, auto_now=False, auto_now_add=False)
    
    class Meta():
        db_table = 'pessoa_juridica'