# Generated by Django 3.2 on 2021-12-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
