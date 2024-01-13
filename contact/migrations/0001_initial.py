# Generated by Django 4.2.8 on 2024-01-09 23:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('mobile', models.CharField(max_length=12)),
                ('email', models.CharField()),
                ('compañia', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]