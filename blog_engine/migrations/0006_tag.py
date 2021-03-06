# Generated by Django 2.1.7 on 2019-03-25 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_engine', '0005_auto_20190320_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('topics', models.ManyToManyField(related_name='tags', to='blog_engine.Topic')),
            ],
        ),
    ]
