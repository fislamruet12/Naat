# Generated by Django 2.1 on 2018-08-26 16:18

import Hamd.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hamd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='artist_photo',
            field=models.FileField(null=True, upload_to=Hamd.models.get_upload_file),
        ),
    ]
