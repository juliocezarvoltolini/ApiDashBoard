from .empresa import Empresa
from django.db import models
from .pessoa import Pessoa

class Operacao(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    codigo_origem = models.TextField(max_length=200)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)    
    descricao_operacao = models.CharField(max_length=50)
    cliente = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField(null=True, blank=True)
    data_expedicao = models.DateTimeField(null=True, blank=True)
    data_faturamento = models.DateTimeField(null=True, blank=True)
    vl_bruto_servico = models.DecimalField(max_digits=13, decimal_places=4)
    vl_bruto_produto = models.DecimalField(max_digits=13, decimal_places=4)
    vl_bruto = models.DecimalField(max_digits=13, decimal_places=4)
    vl_desconto_servico = models.DecimalField(max_digits=13, decimal_places=4)
    vl_desconto_produto = models.DecimalField(max_digits=13, decimal_places=4)
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
        db_table = "operacao"
        
        