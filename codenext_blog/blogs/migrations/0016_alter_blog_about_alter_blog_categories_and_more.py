# Generated by Django 4.2 on 2024-12-08 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_alter_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blogs.category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
