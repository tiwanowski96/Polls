import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return 'ID: %s, question_text: %s, pub_date: %s' % (self.id, self.question_text, self.pub_date)

    # practice examples below

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def less(self):
        return 'Less details: %s' % (self.question_text)
    
    def choices(self):
        if self.choice_set.count() == 0 :
            return 'There are no choices'
        elif self.choice_set.count() == 1 :
            return 'There is 1 choice: ' + str(self.choice_set.all())
        else :
            return 'There are %s choices: ' % (self.choice_set.count()) + str(self.choice_set.all())

    class Meta:
        app_label = 'polls'