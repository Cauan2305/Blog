# Generated by Django 3.2.8 on 2021-10-27 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_publicação_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='nome',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='texto',
            field=models.TextField(blank=True),
        ),
    ]
