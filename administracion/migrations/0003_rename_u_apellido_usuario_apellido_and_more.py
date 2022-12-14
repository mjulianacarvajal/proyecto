# Generated by Django 4.1.3 on 2022-12-11 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_alter_usuario_u_apellido_alter_usuario_u_direccion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='u_apellido',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='u_direccion',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='u_documento',
            new_name='documento',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='u_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='u_nombre',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='u_telefono',
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
