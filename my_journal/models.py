import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Journal(models.Model):
    title = models.CharField('Optional title', max_length=100)
    entry = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse('journal-detail', kwargs={ 'journal_id': self.id })

class Thought(models.Model):
    thought = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.thought
    
    class Meta:
        ordering = ['pub_date']
    
