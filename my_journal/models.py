import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Journal(models.Model):
    title = models.CharField('Optional title', max_length=100)
    entry = models.TextField()
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)