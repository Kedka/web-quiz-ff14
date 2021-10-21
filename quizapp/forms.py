from django.forms import ModelForm
from .models import *

class addQuestionForm(ModelForm):
    class Meta:
        model=QuestionModel
        fields='__all__'