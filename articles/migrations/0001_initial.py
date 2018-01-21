# Generated by Django 2.0.1 on 2018-01-21 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('author', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('picture', models.ImageField(blank=True, upload_to='media/', verbose_name='img')),
                ('featured', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
