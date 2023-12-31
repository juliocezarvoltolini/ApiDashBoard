# Generated by Django 4.2.6 on 2023-10-30 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardApi', '0004_rename_id_empresa_venda_empresa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='id_produto_cliente',
            new_name='codigo_origem',
        ),
        migrations.RenameField(
            model_name='venda',
            old_name='id_venda_cliente',
            new_name='codigo_origem',
        ),
        migrations.RenameField(
            model_name='vendaitem',
            old_name='id_produto',
            new_name='produto',
        ),
        migrations.RenameField(
            model_name='vendaitem',
            old_name='id_venda',
            new_name='venda',
        ),
    ]
