from django.db import models
from .uf import UF
from .validators import cpf_validator



class PessoaFisica(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True, validators=[cpf_validator])
    data_nascimento = models.DateField(null=True, auto_now=False, auto_now_add=False)
    registro_geral_numero = models.CharField(max_length=50)
    registro_geral_sigla_emissor = models.CharField(max_length=10)
    
    class Meta():
        db_table = 'pessoa_fisica'
    