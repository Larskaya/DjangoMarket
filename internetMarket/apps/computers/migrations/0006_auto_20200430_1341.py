# Generated by Django 2.1.5 on 2020-04-30 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0005_auto_20200430_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computer',
            old_name='value',
            new_name='computer value',
        ),
    ]
