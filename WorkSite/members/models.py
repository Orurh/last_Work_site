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

    name = models.CharField(max_length=255, verbose_name='Ф.И.О')
    slug = AutoSlugField(populate_from='name', max_length=255, unique=True, db_index=True, verbose_name='слаг')
    # slug = models.SlugField(max_length=255, unique=True, db_index=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None, blank=True, null=True, verbose_name='Фото')
    rank = models.CharField(max_length=100, verbose_name='Звание')
    position = models.CharField(max_length=255, verbose_name='Должность')
    reference = models.TextField(blank=True, verbose_name='Cправка-отзыв')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_public = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                    default=Status.CHERNOVIK, verbose_name='Статус')
    pos = models.ForeignKey('Positions', on_delete=models.PROTECT, related_name='pos',
                            verbose_name='Категория')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags', verbose_name='Тэги')
    duties = models.OneToOneField('Duties', on_delete=models.SET_NULL, null=True, blank=True, related_name='memb',
                                  verbose_name='Исполняемая должность')

    objects = models.Manager()
    # если не определить, то перестает работать после добавления PublishedManager(), так же лучше прописывать
    # перед доп методом в тек. случае published
    published = PublishedManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудники СПТ'
        verbose_name_plural = 'Сотрудники СПТ'

    def get_absolute_url(self):
        '''абсолютный URL, для использования слага из модели'''
        return reverse('members', kwargs={'post_slug': self.slug})


class Positions(models.Model):  # разбиваем по должностям
    title = models.CharField(max_length=100, db_index=True)
    slug = AutoSlugField(populate_from='title', unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        '''абсолютный URL, для использования слага из модели'''
        return reverse('categories', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class TagPost(models.Model):
    objects = models.Manager()
    tag = models.CharField(max_length=100, db_index=True)
    slug = AutoSlugField(populate_from='tag', unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        '''абсолютный URL, для использования слага из модели'''
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Duties(models.Model):
    name = models.CharField(max_length=100)
    term = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')
