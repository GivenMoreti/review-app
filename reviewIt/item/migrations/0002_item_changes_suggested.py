# Generated by Django 5.0.7 on 2024-08-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='changes_suggested',
            field=models.TextField(default=None),
        ),
    ]
