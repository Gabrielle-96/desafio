# Generated by Django 4.1.7 on 2023-02-15 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
            ],
            options={
                'verbose_name': 'Mensagen',
                'db_table': 'mensagens',
            },
        ),
    ]
