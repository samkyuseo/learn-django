import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model): 
    question_text = models.CharField(max_length=200) # fields correspond to columns in a table 
    pub_date = models.DateTimeField('date published') # optional human readable format 

    def __str__(self): 
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.delta(day=1)

class Choice(models.Model): 
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Choice is related to a single question
    choice_text = models.CharField(max_length=200) # different field classes tell django the type of the field
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text