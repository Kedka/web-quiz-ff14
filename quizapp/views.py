from quizapp.models import QuestionModel
from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def quiz(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuestionModel.objects.all()
        wrong=0
        correct=0
        answers = []
        for q in questions:
            if q.answer == request.POST.get(q.question):
                correct+=1
            else:
                wrong+=1
            answers.append(request.POST.get(q.question))
        # print(answers)

        arr = zip(answers, questions)
        # print(list(arr))
        context = {
            'correct':correct,
            'wrong':wrong,
            'xD':arr
            # 'questions':questions,
            # 'check': answers
        }
        return render(request,'result.html',context)
    else:
        questions=QuestionModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'quiz.html',context)

def home(request):
    return render(request, 'home.html')