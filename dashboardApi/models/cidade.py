from django.db import models

from dashboardApi.models.uf import UF

class Cidade(models.Model):
    id = models.BigAutoField(primary_key=True)
    uf = models.ForeignKey(UF, on_delete=models.RESTRICT)
    nome = models.CharField(max_length=60)
    
    class Meta():
        db_table = "cidade"
        constraints = [models.UniqueConstraint(fields=["uf", "nome"], name="Cidade já cadastrada para a UF informada.")]