
from django.db import models
import uuid
from .pessoa_fisica import PessoaFisica
from .pessoa_juridica import PessoaJuridica

class Pessoa(models.Model):
    
    class IndicadorPessoa(models.TextChoices):
        PESSOA_FISICA = "PF"
        PESSOA_JURIDICA = "PJ"
        PRODUTOR_RURAL = "PR"
        CONSUMIDOR_NAO_IDENTIFICADO = "C"
    
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4)
    codigo_origem = models.CharField(max_length=50, name="codigo_cliente", db_index=True)
    nome = models.CharField(max_length=150, help_text="Pode ser o primeiro nome da pessoa física ou razão social")
    sobrenome = models.CharField(max_length=150, help_text="sobrenome da pessoa física")
    nome_fantasia = models.CharField(max_length=150, help_text="Nome fantasia da empresa ou apelido da pessoa física")
    pessoa_fisica = models.OneToOneField(PessoaFisica,  null=True, blank=True, on_delete=models.CASCADE)
    pessoa_juridica = models.OneToOneField(PessoaJuridica,  null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta():
        db_table = 'pessoa'
    
    