import datetime
from django.db import models
from django.forms import ModelForm
from autoslug import AutoSlugField
from django.db.models import F


# Create your models here.


class Fire(models.Model):
    datetime = models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время')
    message_from = models.ForeignKey('MessageFrom', default=1,
                                     on_delete=models.PROTECT, related_name='message',
                                     verbose_name='Сообщение от')
    unitarea = models.ForeignKey('UnitArea', default=1,
                                 on_delete=models.PROTECT, related_name='unitarea',
                                 verbose_name='Район выезда')
    adress = models.CharField(max_length=150, verbose_name='Адрес')
    rankfire = models.ForeignKey('RankFire', default=1,
                                 on_delete=models.PROTECT, related_name='rankfire',
                                 verbose_name='Ранг пожара')

class MessageFrom(models.Model):  # откуда поступило сообщение
    message_from = models.CharField(max_length=150, db_index=True)
    slug = AutoSlugField(populate_from='message_from', unique=True, db_index=True)

    def __str__(self):
        return self.message_from


class UnitArea(models.Model): # район выезда подразделения
    name = models.CharField(max_length=150, db_index=True)
    slug = AutoSlugField(populate_from='name', unique=True, db_index=True)

    def __str__(self):
        return self.name

class RankFire(models.Model):
    rank = models.CharField(max_length=10, db_index=True)
    slug = AutoSlugField(populate_from='rank', unique=True, db_index=True)

    def __str__(self):
        return self.rank