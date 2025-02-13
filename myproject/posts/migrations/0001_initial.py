# Generated by Django 5.1.6 on 2025-02-12 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('slug', models.SlugField(max_length=120)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
