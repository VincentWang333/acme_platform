# Generated by Django 3.2.10 on 2021-12-20 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acme_api', '0002_auto_20211220_2331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iotfridge',
            old_name='wate_leak',
            new_name='water_leak',
        ),
    ]
