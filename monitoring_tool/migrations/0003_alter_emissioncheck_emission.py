# Generated by Django 3.2.22 on 2023-10-11 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_tool', '0002_emissionchecks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emissioncheck',
            name='emission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emissioncheck', to='monitoring_tool.emission'),
        ),
    ]
