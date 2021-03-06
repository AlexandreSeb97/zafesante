# Generated by Django 2.0.1 on 2018-03-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20180311_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='author',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='questions',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
