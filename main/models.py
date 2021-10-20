from django.db import models
from datetime import datetime
from django.conf import settings
from django.db.models.signals import pre_save, m2m_changed
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

import main.const


class Survey(models.Model):
    name = models.CharField(default='', max_length=100, db_index=True, unique=True,
                            verbose_name='Название')

    description = models.CharField(max_length=10000, db_index=True, unique=False,
                                   verbose_name='Описание')

    start_date = models.DateTimeField(default=datetime.now)

    end_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Опросы'
        verbose_name = 'Опрос'
        ordering = ['-start_date']


class Question(models.Model):
    survey = models.ForeignKey('Survey',
                               on_delete=models.PROTECT, null=False, blank=False,
                               verbose_name='Опрос')

    text = models.CharField(max_length=10000, db_index=True, unique=False,
                            verbose_name='Текст вопроса')

    type = models.PositiveSmallIntegerField(choices=main.const.TYPE_CHOICES, default=main.const.TEXT,
                                            verbose_name='Тип')

    answer_options = models.CharField(max_length=10000, db_index=True, unique=False,
                                      verbose_name='Варианты ответа', null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'
        ordering = ['survey']


class Survey_result(models.Model):
    user = models.IntegerField(default=0, verbose_name='Пользователь')

    survey = models.ForeignKey('Survey',
                               on_delete=models.PROTECT, null=False, blank=False,
                               verbose_name='Опрос')

    question = models.ForeignKey('Question',
                                 on_delete=models.PROTECT, null=False, blank=False,
                                 verbose_name='Вопрос')

    answer = models.CharField(max_length=1000, db_index=True, unique=False,
                              verbose_name='Ответ')

    def __str__(self):
        return "{user} : {name} : {question} : {answer}".format(
            user=self.user,
            name=self.survey.name,
            question=self.question.text,
            answer=self.answer
        )

    class Meta:
        verbose_name_plural = 'Результаты'
        verbose_name = 'Результат'
        ordering = ['survey']
        unique_together = (('user', 'survey', 'question'),)


@receiver(pre_save, sender=Survey)
def date_start_freezer(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass  # Initial save -- do nothing
    else:
        if not obj.start_date == instance.start_date:  # Field has changed
            raise models.ProtectedError('`start_date` should not be modified')
