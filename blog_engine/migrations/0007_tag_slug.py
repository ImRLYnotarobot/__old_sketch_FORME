# Generated by Django 2.1.7 on 2019-03-26 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_engine', '0006_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=None, max_length=15, unique=True),
            preserve_default=False,
        ),
    ]
