# Generated by Django 4.2 on 2024-11-17 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(to='blogs.category'),
        ),
    ]