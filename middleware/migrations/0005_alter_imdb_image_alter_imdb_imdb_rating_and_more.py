# Generated by Django 4.0.3 on 2022-03-28 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('middleware', '0004_alter_imdb_directors_alter_imdb_plot_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imdb',
            name='image',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='imdb',
            name='imdb_rating',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='imdb',
            name='runtimeStr',
            field=models.CharField(max_length=20, null=True),
        ),
    ]