# Generated by Django 2.0.2 on 2019-07-26 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190726_1137'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='jobs',
            new_name='Job',
        ),
    ]
