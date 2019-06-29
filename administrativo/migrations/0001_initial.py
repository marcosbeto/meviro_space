# Generated by Django 2.1.5 on 2019-06-21 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('infra', '0001_initial'),
        ('educacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Contrato',
                'verbose_name_plural': 'Contratos',
            },
        ),
        migrations.CreateModel(
            name='NotaFiscal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacao', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=50)),
                ('fornecedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='infra.Fornecedor')),
            ],
            options={
                'verbose_name': 'Nota Fiscal',
                'verbose_name_plural': 'Notas Fiscais',
            },
        ),
        migrations.CreateModel(
            name='Pacote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.TextField(null=True)),
                ('data_implantacao', models.DateField()),
                ('ultima_atualizacao', models.DateField(blank=True)),
                ('valor_recorrente', models.DecimalField(decimal_places=2, max_digits=6)),
                ('valor_unico', models.DecimalField(decimal_places=2, max_digits=6)),
                ('horas_por_credito', models.IntegerField(blank=True)),
                ('valor_periodo_minimo', models.IntegerField(blank=True)),
                ('tipo_periodo_minimo', models.CharField(choices=[('Horas', 'horas'), ('Dias', 'dias'), ('Semanas', 'semanas'), ('Meses', 'meses')], max_length=256)),
                ('observacoes', models.TextField(null=True)),
                ('pode_agendar_maquinas', models.BooleanField(default=True)),
                ('assinantes_tem_desconto_recurso', models.BooleanField(default=False)),
                ('desconto_recurso_percentual', models.IntegerField(blank=True)),
                ('desconto_recurso_valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('contrato', models.ManyToManyField(to='administrativo.Contrato')),
                ('curso', models.ManyToManyField(to='educacao.Curso')),
                ('outraAtividade', models.ManyToManyField(to='educacao.OutraAtividade')),
            ],
            options={
                'verbose_name': 'Pacote',
                'verbose_name_plural': 'Pacotes',
            },
        ),
        migrations.CreateModel(
            name='PeriodosReservaRecurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Período para Reseva',
                'verbose_name_plural': 'Períodos para Resevas',
            },
        ),
        migrations.CreateModel(
            name='Regra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodosReservaRecurso', models.ManyToManyField(to='administrativo.PeriodosReservaRecurso')),
                ('recurso', models.ManyToManyField(to='infra.Recurso')),
            ],
            options={
                'verbose_name': 'Regra',
                'verbose_name_plural': 'Regras',
            },
        ),
        migrations.AddField(
            model_name='pacote',
            name='regra',
            field=models.ManyToManyField(to='administrativo.Regra'),
        ),
    ]
