# Generated by Django 3.2 on 2021-12-23 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0004_alter_visit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 23, 16, 15, 6, 517363)),
        ),
    ]