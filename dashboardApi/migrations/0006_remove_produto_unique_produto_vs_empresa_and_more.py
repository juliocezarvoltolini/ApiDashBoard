# Generated by Django 4.2.6 on 2023-10-30 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardApi', '0005_rename_id_produto_cliente_produto_codigo_origem_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='produto',
            name='Unique Produto vs Empresa',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='id_empresa',
            new_name='empresa',
        ),
        migrations.AddConstraint(
            model_name='produto',
            constraint=models.UniqueConstraint(fields=('empresa', 'codigo_origem'), name='Unique Produto vs Empresa'),
        ),
    ]
