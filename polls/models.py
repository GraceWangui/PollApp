import datetime
import uuid


from django.db import models
from django.utils import timezone

# Create your models here.

class CommonInfo(models.Model):
      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    

      class Meta:
        abstract = True

class Question(CommonInfo):
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
  

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(CommonInfo):
   
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

