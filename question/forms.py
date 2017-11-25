from django import forms

from .models import CalculationQuestion

class CalculationQuestionForm(forms.ModelForm):

    class Meta:
        model = CalculationQuestion
        fields = ('title', 'text', 'imager')