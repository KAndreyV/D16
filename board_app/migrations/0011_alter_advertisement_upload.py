# Generated by Django 4.1.2 on 2022-11-03 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0010_alter_advertisement_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to='content'),
        ),
    ]
