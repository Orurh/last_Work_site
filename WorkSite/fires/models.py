import datetime
from django.db import models
from django.forms import ModelForm
from autoslug import AutoSlugField
from django.urls import reverse


# Create your models here.


class Fire(models.Model):
    datetime = models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время')
    slug = AutoSlugField(populate_from='adress', max_length=255, unique=True, db_index=True, verbose_name='слаг')
    message_from = models.ForeignKey('MessageFrom', default=1,
                                     on_delete=models.PROTECT, related_name='message',
                                     verbose_name='Сообщение от')
    unitarea = models.ForeignKey('UnitArea', default=1,
                                 on_delete=models.PROTECT, related_name='unitarea',
                                 verbose_name='Район выезда')
    adress = models.CharField(max_length=150, verbose_name='Адрес', db_index=True)
    rankfire = models.ForeignKey('RankFire', default=1, db_index=True,
                                 on_delete=models.PROTECT, related_name='rankfire',
                                 verbose_name='Ранг пожара')
    rtp = models.ForeignKey('LastRtp', default=3,
                            on_delete=models.PROTECT, related_name='rtp',
                            verbose_name='Последний РТП')
    time_come = models.IntegerField(blank=True, null=True, verbose_name='Время прибытия')
    time_fire_hose = models.IntegerField(blank=True, null=True, verbose_name='Время подачи ствола')
    time_loc = models.IntegerField(blank=True, null=True, verbose_name='Время локализации')
    time_elim = models.IntegerField(blank=True, null=True, verbose_name='Время ликвидации')
    fire_area = models.IntegerField(blank=True, null=True, verbose_name='Площадь пожара')
    gdzsunits = models.ForeignKey('GdzsUnits', default=1,
                            on_delete=models.PROTECT, related_name='gdzsunits',
                            verbose_name='Звенья ГДЗС')

    class Meta:
        verbose_name = 'Пожар'
        verbose_name_plural = 'Пожары'

    def get_absolute_url(self):
        '''абсолютный URL, для использования слага из модели'''
        return reverse('fire', kwargs={'fire_slug': self.slug})


class MessageFrom(models.Model):  # откуда поступило сообщение
    message_from = models.CharField(max_length=150, db_index=True)
    slug = AutoSlugField(populate_from='message_from', unique=True, db_index=True)

    def __str__(self):
        return self.message_from


class UnitArea(models.Model):  # район выезда подразделения
    name = models.CharField(max_length=150, db_index=True)
    slug = AutoSlugField(populate_from='name', unique=True, db_index=True)

    def __str__(self):
        return self.name


class RankFire(models.Model):
    rank = models.CharField(max_length=10, db_index=True)
    slug = AutoSlugField(populate_from='rank', unique=True, db_index=True)

    def __str__(self):
        return self.rank


class LastRtp(models.Model):
    lastrtp = models.CharField(max_length=10, db_index=True)
    slug = AutoSlugField(populate_from='lastrtp', unique=True, db_index=True)

    def __str__(self):
        return self.lastrtp


class GdzsUnits(models.Model):
    quantity = models.CharField(max_length=20, db_index=True)
    slug = AutoSlugField(populate_from='quantity', unique=True, db_index=True)

    def __str__(self):
        return self.quantity
