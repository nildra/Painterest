# Generated by Django 5.0.4 on 2024-04-11 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_usersdb_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostsDB',
            fields=[
                ('id_post', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('pathImg', models.CharField(max_length=255)),
                ('id_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.usersdb')),
            ],
        ),
    ]
