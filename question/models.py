from django.db import models

from utils.base_models import BaseModel, ID


class Questionnaire(BaseModel, ID):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    form = models.JSONField(null=True, blank=True)
    flutter_json = models.JSONField(null=True, blank=True)


class Question(BaseModel):
    class QuestionTypeChoices(models.TextChoices):
        RADIOGROUP = "radiogroup"
        TEXT = "text"
        BOOLEAN = "boolean"

    class InputTypeChoices(models.TextChoices):
        DATE = "date"
        NUMBER = "number"
        TEXT = "text"

    questionnaire = models.ForeignKey(to=Questionnaire, on_delete=models.PROTECT, related_name='questions')

    question_type = models.CharField(max_length=15, choices=QuestionTypeChoices.choices)
    input_type = models.CharField(max_length=10, choices=InputTypeChoices.choices, null=True, blank=True)

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=100, null=True, blank=True)  # Description in survey.js forms


class Option(BaseModel):
    question = models.ForeignKey(to=Question, on_delete=models.PROTECT, related_name='options')
    answer = models.ManyToManyField(to=Questionnaire, related_name='options')

    value = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Condition(BaseModel):
    class OperatorChoices(models.TextChoices):
        GREATER_THAN = ">"
        LESS_THAN = "<"
        GREATER_THAN_OR_EQUAL = ">="
        LESS_THAN_OR_EQUAL = "<="
        EQUAL = "=="
        NOT_EQUAL = "!="

    question = models.ForeignKey(to=Question, on_delete=models.PROTECT, related_name='conditions')
    operator = models.CharField(choices=OperatorChoices.choices, max_length=2, null=True, blank=True)
    next_question = models.ForeignKey(to=Question, on_delete=models.PROTECT, related_name='next_conditions')
    prescription = models.TextField(null=True, blank=True)


class MultiCondition(BaseModel):
    class OperatorChoices(models.TextChoices):
        AND = "and"
        OR = "or"

    conditions = models.ManyToManyField(to=Condition, related_name='multi_conditions')
    logical_operator = models.CharField(choices=OperatorChoices.choices, max_length=3, default='AND')
