# Generated by Django 3.2.22 on 2023-10-22 20:46

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('location', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('emission_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('description', models.TextField(blank=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_checked', models.DateTimeField(auto_now=True)),
                ('next_check_due', models.DateField()),
                ('current_check_due', models.DateField()),
                ('status', models.IntegerField(choices=[(0, 'Open'), (1, 'Closed')], default=0)),
                ('type', models.IntegerField(choices=[(1, 'Weep'), (2, 'Seep'), (3, 'Fugitive Emission')], default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monitoring_tool_emissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='EmissionCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_checked', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'None Detected'), (2, 'Below Minimum Threshold'), (3, 'Above Minimum Threshold')], default=0)),
                ('comments', models.TextField()),
                ('checked_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emissioncheck', to='monitoring_tool.emission')),
            ],
        ),
    ]
