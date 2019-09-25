from django.shortcuts import render

# Create your views here.
from .models import Question, Choice


#get questions and display them
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'lastest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)