# Generated by Django 2.1.5 on 2019-03-15 17:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20190315_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tictactoe',
            name='board',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=[0, 0, 0, 0, 0, 0, 0, 0, 0], size=None),
        ),
    ]
