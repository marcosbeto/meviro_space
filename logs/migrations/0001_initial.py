# Generated by Django 2.1.5 on 2020-02-06 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios_meviro', '0001_initial'),
        ('infra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogAcessoEspacoUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateField(blank=True, null=True)),
                ('hora_entrada', models.TimeField(blank=True, null=True)),
                ('data_saida', models.DateField(blank=True, null=True)),
                ('hora_saida', models.TimeField(blank=True, null=True)),
                ('id_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios_meviro.UsuarioEspaco')),
            ],
            options={
                'verbose_name': 'Registro de Log de Acesso',
                'verbose_name_plural': 'Logs de Acesso',
            },
        ),
        migrations.CreateModel(
            name='LogUsoFerramentaUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_ativacao', models.DateField(blank=True, null=True)),
                ('hora_ativacao', models.TimeField(blank=True, null=True)),
                ('data_desativacao', models.DateField(blank=True, null=True)),
                ('hora_desativacao', models.TimeField(blank=True, null=True)),
                ('tempo_uso', models.TimeField(blank=True, null=True)),
                ('id_bridge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='infra.Bridge')),
                ('id_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios_meviro.UsuarioEspaco')),
            ],
            options={
                'verbose_name': 'Registro de Log de Uso',
                'verbose_name_plural': 'Logs de Uso',
            },
        ),
    ]
