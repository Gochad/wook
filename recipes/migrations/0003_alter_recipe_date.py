# Generated by Django 4.2 on 2023-04-05 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 4, 5, 10, 53, 17, 387321)),
        ),
    ]
