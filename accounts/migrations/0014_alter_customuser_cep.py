# Generated by Django 5.0.1 on 2024-04-02 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_customuser_bairro_alter_customuser_cep_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cep',
            field=models.CharField(default='nenhum', max_length=20),
        ),
    ]