# Generated by Django 2.1.7 on 2019-03-17 08:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_engine', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Blog',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
