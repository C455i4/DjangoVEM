# Generated by Django 5.0.1 on 2024-04-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_customuser_cep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cep',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
