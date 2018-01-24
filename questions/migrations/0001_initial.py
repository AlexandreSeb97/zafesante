# Generated by Django 2.0.1 on 2018-01-22 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=510, unique=True)),
                ('author', models.CharField(max_length=50)),
                ('votes', models.IntegerField(default='0')),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]