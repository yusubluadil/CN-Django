# Generated by Django 4.2 on 2024-11-09 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_tag'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
