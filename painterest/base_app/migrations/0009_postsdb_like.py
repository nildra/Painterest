# Generated by Django 5.0.4 on 2024-04-12 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0008_postsdb_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='postsdb',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
