# Generated by Django 3.2.8 on 2021-10-26 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_comentarios_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarios',
            name='usuario',
        ),
        migrations.AddField(
            model_name='comentarios',
            name='nome',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
