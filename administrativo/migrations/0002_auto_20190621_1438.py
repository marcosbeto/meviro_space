# Generated by Django 2.1.5 on 2019-06-21 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='arquivo',
            field=models.ImageField(blank=True, upload_to='arquivos/contratos'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='descricao',
            field=models.TextField(null=True),
        ),
    ]
