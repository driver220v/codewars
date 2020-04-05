from django.db import models
from django.utils import timezone


class BD(models.Model):
    title = models.CharField(max_length=100, verbose_name='Name of a task')
    content = models.TextField(null=False, blank=False, verbose_name='Description')
    author = models.CharField(max_length=50, blank=True, verbose_name='author of a task')
    date_posted = models.DateTimeField(default=timezone.now(), verbose_name='Issue date')

    class Meta:
        verbose_name_plural = 'Computer Science Task'
        verbose_name = 'Computer Science Task'
        ordering = ['-date_posted']
