# Generated by Django 3.2.22 on 2023-10-18 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_tool', '0002_remove_emissioncheck_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emissioncheck',
            old_name='emission',
            new_name='title',
        ),
    ]
