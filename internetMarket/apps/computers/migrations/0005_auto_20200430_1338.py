# Generated by Django 2.1.5 on 2020-04-30 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0004_remove_computer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computer',
            old_name='cpu_frequency',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='price',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='processor',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='processor_cores',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='ram_size',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='ram_type',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='ssd_capacity',
        ),
    ]
