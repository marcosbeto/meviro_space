# Generated by Django 2.1.5 on 2019-07-31 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0008_outrosprodutos_servico'),
        ('usuarios_meviro', '0004_auto_20190624_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditoPorUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Este plano está ativo?')),
                ('data_compra', models.DateField(verbose_name='Data de Ativação')),
                ('data_encerramento', models.DateField(verbose_name='Data de Encerramento')),
                ('id_venda', models.IntegerField(blank=True, null=True, verbose_name='ID Venda ContaAzul')),
                ('numero_creditos', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='administrativo.Pacote', verbose_name='Pacote')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios_meviro.UsuarioEspaco', verbose_name='Nome do Usuário')),
            ],
            options={
                'verbose_name_plural': 'Créditos por Usuário',
                'verbose_name': 'Crédito por Usuário',
            },
        ),
        migrations.CreateModel(
            name='PacotePorUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(default=False, verbose_name='Este plano está ativo?')),
                ('data_ativacao', models.DateField(verbose_name='Data de Ativação')),
                ('data_encerramento', models.DateField(verbose_name='Data de Encerramento')),
                ('id_venda', models.IntegerField(blank=True, null=True, verbose_name='ID Venda ContaAzul')),
                ('pacote', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='administrativo.Pacote', verbose_name='Pacote')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios_meviro.UsuarioEspaco', verbose_name='Nome do Usuário')),
            ],
            options={
                'verbose_name_plural': 'Pacotes por Usuário',
                'verbose_name': 'Pacote por Usuário',
            },
        ),
    ]
