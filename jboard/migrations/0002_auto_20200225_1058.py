# Generated by Django 3.0.2 on 2020-02-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parsers',
            name='description',
            field=models.TextField(),
        ),
    ]
