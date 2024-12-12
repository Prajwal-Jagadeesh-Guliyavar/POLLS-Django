from django.db import models

# Create your models here.
class Questions(models.Model):
    question_text=models.CharField(max_length=100)
    pub_date=models.DateTimeField("date published")

class Choice(models.Model):
    question=models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    vote=models.IntegerField(default=0)