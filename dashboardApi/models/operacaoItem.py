from .produto import Produto
from .operacao import Operacao
from django.db import models


class OperacaoItem(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    operacao = models.ForeignKey(Operacao, on_delete=models.RESTRICT, db_index=True)
    produto = models.ForeignKey(Produto, on_delete=models.RESTRICT)
    quantidade = models.DecimalField(max_digits=13, decimal_places=4)
    vl_unitario = models.DecimalField(max_digits=13, decimal_places=4)
    vl_bruto = models.DecimalField(max_digits=13, decimal_places=4)
    vl_desconto = models.DecimalField(max_digits=13, decimal_places=4)
    vl_liquido = models.DecimalField(max_digits=13, decimal_places=4)
    vl_base_icms = models.DecimalField(max_digits=13, decimal_places=4)
    vl_icms = models.DecimalField(max_digits=13, decimal_places=4)
    vl_base_substituicao_tributaria = models.DecimalField(max_digits=13, decimal_places=4)
    vl_substituicao_tributaria = models.DecimalField(max_digits=13, decimal_places=4)
    vl_ipi = models.DecimalField(max_digits=13, decimal_places=4)
    vl_cofins = models.DecimalField(max_digits=13, decimal_places=4)
    vl_pis = models.DecimalField(max_digits=13, decimal_places=4)
    
    class Meta:
        db_table = "operacao_item"