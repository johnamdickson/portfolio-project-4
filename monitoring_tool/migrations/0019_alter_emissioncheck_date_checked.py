# Generated by Django 3.2.22 on 2023-11-14 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_tool', '0018_auto_20231114_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emissioncheck',
            name='date_checked',
            field=models.DateTimeField(),
        ),
    ]