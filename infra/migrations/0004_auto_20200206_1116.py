# Generated by Django 2.1.5 on 2020-02-06 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0003_auto_20200206_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='infra.Area'),
        ),
    ]