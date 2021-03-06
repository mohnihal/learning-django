from django.db import models
from datetime import datetime,timedelta
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    def was_published_recently(self):
        now=timezone.now()
        return now >= self.pub_date >= timezone.now()-timedelta(days=1)

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
        
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
