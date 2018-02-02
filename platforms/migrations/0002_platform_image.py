# Generated by Django 2.0 on 2018-01-06 00:21

from django.db import migrations, models
import platforms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('platforms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=platforms.utils.platform_image_upload),
        ),
    ]
