from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_public=Member.Status.PUBLIC)


class Member(models.Model):
    class Status(models.IntegerChoices):
        CHERNOVIK = 0, 'Черновик'
        PUBLIC = 1, 'Опубликовано'


    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', max_length=255, unique=True, db_index=True)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True)
    rank = models.CharField(max_length=100)
    position = models.CharField(max_length=255)
    reference = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(choices=Status.choices, default=Status.CHERNOVIK)
    pos = models.ForeignKey('Positions', on_delete=models.PROTECT, related_name='pos')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')


    objects = models.Manager() #если не определить, то перестает работать после добавления PublishedManager()
    published = PublishedManager()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''абсолютный URL, для использования слага из модели'''
        return reverse('members', kwargs={'post_slug': self.slug})


class Positions(models.Model): # разбиваем по должностям
    title = models.CharField(max_length=100, db_index=True)
    slug = AutoSlugField(populate_from='title', unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        '''абсолютный URL, для использования слага из модели'''
        return reverse('categories', kwargs={'cat_slug': self.slug})

class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = AutoSlugField(populate_from='tag', unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        '''абсолютный URL, для использования слага из модели'''
        return reverse('tag', kwargs={'tag_slug': self.slug})