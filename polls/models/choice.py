from django.db import models
from .question import Question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return 'ID: %s, question_id: %s, choice_text: %s, votes: %s' % (self.id, self.question.id, self.choice_text, self.votes)
    
    class Meta:
        app_label = 'polls'