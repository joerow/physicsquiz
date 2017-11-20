from django.shortcuts import render
from .models import CalculationQuestion
from django.utils import timezone
# Create your views here.


def question_list(request):
    questions = CalculationQuestion.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'question/question_list.html',{'questions': questions})
