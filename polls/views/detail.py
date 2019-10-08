# The old version of the code has been commented

# from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone
from polls.models import Question

# def detail(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     context = {
#         'question': question,
#     }
#     return render(request, 'polls/detail.html', context)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):

        return Question.objects.filter(pub_date__lte=timezone.now())