# Generated by Django 4.1.2 on 2022-11-03 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0006_alter_advertisement_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='upload',
            field=models.FileField(default=None, upload_to='upload/'),
            preserve_default=False,
        ),
    ]