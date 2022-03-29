# Generated by Django 4.0.3 on 2022-03-25 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('imdb_id', models.CharField(max_length=200)),
                ('tmdb_type', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Imdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('runtimeStr', models.CharField(max_length=20)),
                ('trailer', models.CharField(max_length=200)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='middleware.title')),
            ],
        ),
    ]