# Generated by Django 5.0.3 on 2024-03-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(blank=True, max_length=100)),
                ('language', models.CharField(max_length=50)),
                ('subjects', models.TextField(blank=True)),
                ('bookshelves', models.TextField(blank=True)),
                ('download_links', models.JSONField(default=list)),
                ('popularity', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]