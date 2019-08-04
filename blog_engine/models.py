from django.db import models
from django.utils import timezone
from django.db.models import Count
from django.shortcuts import reverse


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=1000, default='')
    subscribers = models.ManyToManyField(User, related_name='subscriptions')

    @classmethod
    def get_sorted_query(cls):
        return cls.objects.annotate(total_likes=Count('topic__likes')).order_by('-total_likes')

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=255)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    body = models.TextField(default='')
    likes = models.ManyToManyField(User, related_name='likes')

    def count_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('topic_detail_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('topic_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('topic_delete_url', kwargs={'id': self.id})

    def get_list_url(self):
        return reverse('blog_detail_url', kwargs={'id': self.blog.id})

    class Meta:
        ordering = ['-created']


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=15, unique=True)
    topics = models.ManyToManyField(Topic, related_name='tags')

    def __str__(self):
        return self.title

    @classmethod
    def get_sorted_query(cls):
        return cls.objects.all()

    def get_list_url(self):
        return reverse('tags_list_url')

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
