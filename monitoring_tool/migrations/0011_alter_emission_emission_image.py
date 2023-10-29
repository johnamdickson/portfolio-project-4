# Generated by Django 3.2.22 on 2023-10-29 02:57

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_tool', '0010_alter_emission_emission_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emission',
            name='emission_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]