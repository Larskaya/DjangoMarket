# Generated by Django 2.1.5 on 2020-04-29 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0003_computer_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='name',
        ),
    ]
