# Generated by Django 4.0.4 on 2022-07-05 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSesiones', '0003_sesion_perfil_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sesion_perfil',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='perfiles'),
        ),
    ]
