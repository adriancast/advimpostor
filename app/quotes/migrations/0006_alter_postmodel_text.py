# Generated by Django 3.2 on 2021-12-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0005_postmodel_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
