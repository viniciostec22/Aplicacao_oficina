# Generated by Django 4.1.2 on 2022-10-24 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_alter_servico_protocolo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriamanutencao',
            name='titulo',
            field=models.CharField(choices=[('TVM', 'Trocar valvula do motor'), ('TO', 'Troca de óleo'), ('B', 'Balanceamento'), ('AL', 'Alinhamento')], max_length=4),
        ),
    ]
