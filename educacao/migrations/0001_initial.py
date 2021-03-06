# Generated by Django 2.1.5 on 2020-02-06 13:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('infra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome do Curso')),
                ('descricao', models.TextField(null=True, verbose_name='Descrição do Curso')),
                ('professores', models.TextField(null=True, verbose_name='Professores do Curso')),
                ('precisa_treinamento', models.BooleanField(default=False, verbose_name='É necessário treinamento em equipamentos?')),
                ('dates', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(), size=None, verbose_name='Quais as datas do curso?')),
                ('observacoes', models.TextField(null=True, verbose_name='Observações')),
            ],
            options={
                'verbose_name_plural': 'Cursos',
                'verbose_name': 'Curso',
            },
        ),
        migrations.CreateModel(
            name='OutraAtividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome da Atividade')),
                ('descricao', models.TextField(null=True, verbose_name='Descrição da Atividade')),
                ('organizadores', models.TextField(null=True, verbose_name='Organizadores da Atividade')),
                ('dates', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(), size=None, verbose_name='Quais as datas da atividade?')),
                ('observacoes', models.TextField(null=True, verbose_name='Observações')),
            ],
            options={
                'verbose_name_plural': 'Outras Atividades',
                'verbose_name': 'Outra Atividade',
            },
        ),
        migrations.CreateModel(
            name='TreinamentoEmEquipamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recurso', models.ManyToManyField(to='infra.Recurso', verbose_name='Recurso utilizado no treinamento')),
            ],
            options={
                'verbose_name_plural': 'Treinamentos em Equipamentos',
                'verbose_name': 'Treinamento em Equipamento',
            },
        ),
        migrations.AddField(
            model_name='outraatividade',
            name='treinamentoEmEquipamentos',
            field=models.ManyToManyField(to='educacao.TreinamentoEmEquipamento', verbose_name='Treinamento em Equipamentos'),
        ),
        migrations.AddField(
            model_name='curso',
            name='treinamentoEmEquipamentos',
            field=models.ManyToManyField(to='educacao.TreinamentoEmEquipamento', verbose_name='Em quais equipamentos?'),
        ),
    ]
