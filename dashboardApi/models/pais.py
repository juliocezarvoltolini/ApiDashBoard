from django.db import models

class Pais(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    nome = models.CharField(max_length=60)
    
    class Meta():
        db_table = 'pais'