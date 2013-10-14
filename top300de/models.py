from django.db import models

# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=100)
    pub_date = models.DateField('date published')


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

