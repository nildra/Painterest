# Generated by Django 5.0.4 on 2024-04-12 17:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0007_commentsdb_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='postsdb',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
