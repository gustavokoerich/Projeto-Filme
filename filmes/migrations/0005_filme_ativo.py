# Generated by Django 4.1.1 on 2022-09-08 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0004_rename_filmes_filme'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='ativo',
            field=models.BooleanField(default=1),
        ),
    ]
