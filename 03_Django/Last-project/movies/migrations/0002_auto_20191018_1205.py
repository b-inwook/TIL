# Generated by Django 2.2.6 on 2019-10-18 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Comments',
        ),
    ]
