# Generated by Django 4.0.4 on 2022-07-06 02:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppSesiones', '0006_alter_sesion_perfil_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sesion_perfil',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sesion_perfil', to=settings.AUTH_USER_MODEL),
        ),
    ]
