from django.db import models

fieldsEmpresa = ["codigo_cliente", "cnpj", "cep", "nome_fantasia", "razao_social"]

class Empresa(models.Model):

    id = models.AutoField(primary_key=True, db_index=True)
    codigo_cliente = models.CharField(max_length=50, null=False, blank=False, default='')
    cnpj = models.CharField(unique=True, max_length=14)
    cep = models.CharField(max_length=8)
    nomeFantasia = models.CharField( default="", name='nome_fantasia', max_length=150)
    razaoSocial = models.CharField( default="", name='razao_social', max_length=150)
    
    
    class Meta:
        db_table = "empresa"
