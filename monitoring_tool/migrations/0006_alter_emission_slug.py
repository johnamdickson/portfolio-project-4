# Generated by Django 3.2.22 on 2023-10-27 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_tool', '0005_alter_emission_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emission',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
