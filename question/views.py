from django.shortcuts import render, get_object_or_404
from .models import CalculationQuestion
from django.utils import timezone
from .forms import CalculationQuestionForm
# Create your views here.


def question_list(request):
    questions = CalculationQuestion.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'question/question_list.html', {'questions': questions})


def question_detail(request, pk):
    question = get_object_or_404(CalculationQuestion, pk=pk)
    return render(request, 'question/question_detail.html', {'question': question})

def question_new(request):
    form = CalculationQuestionForm()
    return render(request, 'question/question_edit.html', {'form': form})
