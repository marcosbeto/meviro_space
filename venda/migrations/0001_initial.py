# Generated by Django 2.1.5 on 2019-06-29 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios_meviro', '0004_auto_20190624_2208'),
        ('administrativo', '0007_auto_20190624_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdemDeServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_os', models.CharField(choices=[('orcamento_pendente', 'Orçamento Pendente'), ('servico_pendente', 'Serviço Pendente'), ('em_andamento', 'Em andamento'), ('concluido', 'Concluído')], default='Orçamento Pendente', max_length=20, verbose_name='Status da OS')),
                ('numero_os', models.IntegerField(blank=True, null=True, verbose_name='Número da OS')),
                ('data_inicio', models.DateField(null=True, verbose_name='Data de início')),
                ('previsao_entrega', models.DateField(blank=True, null=True, verbose_name='Previsão de entrega')),
                ('descricao_servico', models.TextField(blank=True, null=True, verbose_name='Descrição do serviço a ser prestado')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('usuario_meviro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios_meviro.UsuarioEspaco', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Ordem de Serviço',
                'verbose_name_plural': 'Ordens de Serviços',
            },
        ),
        migrations.CreateModel(
            name='VendaCreditos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_venda', models.DateField(blank=True, null=True, verbose_name='Data da Venda')),
                ('numero_venda', models.IntegerField(blank=True, null=True, verbose_name='Número da Venda de Crédito')),
                ('numero_creditos', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade de Créditos')),
                ('contratos', models.ManyToManyField(blank=True, to='administrativo.Contrato')),
                ('usuario_meviro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios_meviro.UsuarioEspaco', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Venda de Crédito',
                'verbose_name_plural': 'Venda de Créditos',
            },
        ),
        migrations.CreateModel(
            name='VendaPacotesPorUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_assinatura', models.DateField(blank=True, null=True, verbose_name='Data da Assinatura')),
                ('numero_venda', models.IntegerField(blank=True, null=True, verbose_name='Número da Venda de Pacote')),
                ('status', models.CharField(choices=[('pagamento_pendente', 'Pagamento Pendente'), ('ativo', 'Ativo'), ('expirado', 'Expirado')], default='Pagamento Pendente', max_length=20, verbose_name='Status')),
                ('contratos', models.ManyToManyField(blank=True, to='administrativo.Contrato')),
                ('pacotes', models.ManyToManyField(blank=True, to='administrativo.Pacote', verbose_name='Pacotes')),
                ('usuario_meviro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios_meviro.UsuarioEspaco', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Venda de Pacote',
                'verbose_name_plural': 'Venda de Pacotes',
            },
        ),
    ]
