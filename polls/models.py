from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin

# Create your models here.
'''class Questions(models.Model):
    question_text=models.CharField(max_length=100)
    #pub_date=models.DateTimeField("date published")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)'''
class Questions(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
    @admin.display(
            boolean= True,
            ordering= "pub_date",
            description="published recently...?",
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <=self.pub_date <=now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


'''class Choice(models.Model):
    question=models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    vote=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text'''
class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
