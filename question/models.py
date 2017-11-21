from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class CalculationQuestion(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    topic = models.CharField(max_length=200)
    answer = models.DecimalField
    imager = models.CharField(max_length=200, blank=True, null=True)
        

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
