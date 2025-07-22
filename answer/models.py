from django.db import models

from core.models import User
from question.models import Questionnaire
from utils.base_models import BaseModel, ID


class AnswerSet(BaseModel, ID):
    patient = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='answer_sets')
    questionnaire = models.ForeignKey(to=Questionnaire, on_delete=models.PROTECT, related_name='answer_sets')
    detail = models.JSONField(null=True, blank=True)


class Answer(BaseModel):
    question = models.ForeignKey(to=Questionnaire, on_delete=models.PROTECT, related_name='answers')
    text = models.CharField(max_length=50, null=True, blank=True)
