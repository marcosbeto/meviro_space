# Generated by Django 2.1.5 on 2020-02-06 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='api_financeiro',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='API financeiro Conta Azul'),
        ),
    ]
