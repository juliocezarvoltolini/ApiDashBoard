from django.db import models

from .cidade import Cidade
from .pessoa import Pessoa



class PessoaEndereco(models.Model):
    
    class IdentificadorEndereco(models.TextChoices):
        FIXO = "FIXO"
        COBRANCA = "COBRANCA"
        OUTRO = "OUTRO"
    
    id = models.BigAutoField(primary_key=True, auto_created=True)
    codigo_origem = models.CharField(max_length=60)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8, help_text="Deve inserir apenas os números do CEP, sem espaços e caracteres especiais.")
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=60)
    cidade = models.ForeignKey(Cidade, on_delete=models.RESTRICT)
    celular = models.CharField(max_length=15, blank=True)
    telefone1 = models.CharField(max_length=15, blank=True)
    telefone2 = models.CharField(max_length=15, blank=True)
    identificador_endereco =  models.CharField(
        max_length=20, 
        choices=IdentificadorEndereco.choices, 
        default=IdentificadorEndereco.FIXO,
        help_text="O endereço pode ser identificado com as seguintes TAGS: FIXO, COBRANCA, OUTRO"
    )
      
    
    class Meta():
        db_table = 'pessoa_endereco'
    