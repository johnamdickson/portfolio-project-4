# Generated by Django 3.2.22 on 2023-11-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_tool', '0015_auto_20231113_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emissioncheck',
            name='comments',
            field=models.TextField(max_length=100),
        ),
    ]
