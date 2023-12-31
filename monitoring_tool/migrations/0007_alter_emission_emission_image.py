# Generated by Django 3.2.22 on 2023-10-29 01:28

import cloudinary.models
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_tool', '0006_alter_emission_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emission',
            name='emission_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'tiff', 'heif'])], verbose_name='image'),
        ),
    ]
