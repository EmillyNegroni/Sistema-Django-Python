# Generated by Django 2.1.7 on 2019-07-26 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20190725_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ideias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, unique=True, verbose_name=' Nome da ideia ')),
                ('descricao', models.TextField(verbose_name='Descreva sua ideia')),
                ('categorias', models.CharField(choices=[('TERRA_PLANA', 'Terra plana'), ('CONTRA_GROGER', 'Ideias para coach Groger'), ('CONTRA_JOAO', 'ideias  contra João'), ('PÚBLICAS', 'Públicas'), ('OUTROS', 'Outros')], max_length=255, verbose_name='categorias')),
                ('categorias_outros', models.CharField(blank=True, max_length=225, null=True, verbose_name='caso outros, qual')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_de_atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='data_de_criacao',
        ),
        migrations.AddField(
            model_name='ideias',
            name='pessoa',
            field=models.ForeignKey(on_delete=None, to='website.Pessoa'),
        ),
    ]
