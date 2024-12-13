from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Questions(models.Model):
    question_text=models.CharField(max_length=100)
    #pub_date=models.DateTimeField("date published")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question=models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    vote=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text