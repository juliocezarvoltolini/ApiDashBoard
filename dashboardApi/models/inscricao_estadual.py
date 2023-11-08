from django.db import models

from .pessoa_endereco import PessoaEndereco
from .pessoa import Pessoa
from .uf import UF
 
class InscricaoEstadual(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    inscricao_estadual = models.CharField(max_length=50, unique=True, )
    uf = models.ForeignKey(UF, on_delete=models.RESTRICT)
    endereco = models.OneToOneField(PessoaEndereco, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    
    class Meta():
        db_table = 'inscricao_estadual'