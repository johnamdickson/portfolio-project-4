# Generated by Django 3.2.22 on 2023-10-30 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_tool', '0011_alter_emission_emission_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='emission',
            name='closed_by',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
