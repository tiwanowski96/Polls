from django.shortcuts import get_object_or_404, render
from polls.models import Question

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
        }
    return render(request, 'polls/results.html', context)