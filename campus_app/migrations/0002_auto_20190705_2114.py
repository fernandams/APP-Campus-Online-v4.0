# Generated by Django 2.2.2 on 2019-07-06 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='data_publicacao',
            field=models.DateTimeField(),
        ),
    ]
