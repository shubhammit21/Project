# Generated by Django 2.2.7 on 2020-05-02 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='fileupload',
            new_name='files',
        ),
    ]
