# Generated by Django 5.1.5 on 2025-02-15 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('app', '0005_rename_register_reg'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reg',
            new_name='Newuser',
        ),
    ]
