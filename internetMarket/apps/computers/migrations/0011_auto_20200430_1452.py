# Generated by Django 2.1.5 on 2020-04-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0010_auto_20200430_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]