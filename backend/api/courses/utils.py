from .models import Question
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_question(question: Question):
    answers = question.answers
    num_true = 0
    for ans in answers.all():
        if ans.is_true_answer:
            num_true += 1

    if num_true > 1:
        raise ValidationError(_("Please provide only one valid answer to proceed."))
