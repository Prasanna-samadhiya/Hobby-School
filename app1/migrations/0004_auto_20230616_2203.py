# Generated by Django 3.1.6 on 2023-06-17 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_batch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batch',
            old_name='nm',
            new_name='rnm',
        ),
    ]
