# Generated by Django 5.0.1 on 2024-04-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_bairro_alter_customuser_cep_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bairro',
            field=models.CharField(default='Não especificado', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cep',
            field=models.IntegerField(default='Não especificado'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cidade',
            field=models.CharField(default='Não especificado', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='complemento',
            field=models.CharField(blank=True, default='Nenhum', max_length=200),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cpf',
            field=models.IntegerField(default='Não especificado'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='Não especificado', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='endereco',
            field=models.CharField(default='Não especificado', max_length=200),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='nome',
            field=models.CharField(default='Não especificado', max_length=200),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='numero',
            field=models.CharField(default='Não especificado', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telefone',
            field=models.IntegerField(default='Não especificado'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='uf',
            field=models.CharField(default='Não especificado', max_length=10),
        ),
    ]
