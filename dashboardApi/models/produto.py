import uuid
from django.db import models

from .empresa import Empresa


class Produto(models.Model):    
    
    class ProdutoOuServico(models.TextChoices):
        PRODUTO = "PR"
        SERVICO = "SR"
   
    
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4)
    codigo_origem = models.CharField(max_length=200)
    id_sku = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    ean = models.CharField(max_length=14)
    descricao = models.CharField(max_length=150)
    produto_ou_servico = models.CharField(
        max_length=2, 
        choices=ProdutoOuServico.choices, 
        default=ProdutoOuServico.PRODUTO
    )
    vl_compra = models.DecimalField(max_digits=13, decimal_places=4, null=False, blank=False)
    vl_custo = models.DecimalField(max_digits=13, decimal_places=4, null=False, blank=False)
    vl_venda = models.DecimalField(max_digits=13, decimal_places=4, null=False, blank=False)

    class Meta:
        db_table = "produto"
        constraints = [models.UniqueConstraint(fields=["empresa", "codigo_origem"], name="Unique Produto vs Empresa")]        
        

    def __str__(self):
        return self.id_produto_cliente + " - " + str(self.id_empresa) + " - " + self.descricao 
