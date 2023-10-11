# Generated by Django 3.2.22 on 2023-10-11 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monitoring_tool', '0003_alter_emissioncheck_emission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emissioncheck',
            name='checked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
