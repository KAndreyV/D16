# Generated by Django 4.1.2 on 2022-11-03 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0003_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]