from django.http import HttpResponse

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)