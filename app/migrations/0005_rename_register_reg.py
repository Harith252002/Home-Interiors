# Generated by Django 5.1.5 on 2025-02-15 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('app', '0004_register_delete_reg'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='Reg',
        ),
    ]
