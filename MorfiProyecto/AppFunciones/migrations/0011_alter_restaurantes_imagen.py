# Generated by Django 4.0.4 on 2022-07-04 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFunciones', '0010_rename_nombre_comentario_nombre_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantes',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
