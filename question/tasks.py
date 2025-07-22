from celery import shared_task
from django.db import transaction

from question.models import Questionnaire, Question, Option


@shared_task
@transaction.atomic
class Builder:
    def __init__(self, survey_json):
        self.survey_json = survey_json
        self.questionnaire_instance = None

    def build(self):
        self.create_questionnaire()
        self.create_question()

    def create_questionnaire(self):
        title = self.survey_json.get('title', 'no title')
        description = self.survey_json.get('description', None)

        self.questionnaire_instance = Questionnaire.objects.create(title=title, description=description)

    def create_question(self):
        pages = self.survey_json.get('pages', [])
        for page in pages:
            elements = page.get('elements', [])
            for element in elements:
                self._create_question_of_type(element)

    def _create_question_of_type(self, element):
        question_type = element.get('type')
        input_type = element.get('inputType', None)

        if question_type == Question.QuestionTypeChoices.TEXT and input_type == Question.InputTypeChoices.DATE:
            self._create_date_question(element)

        if question_type == Question.QuestionTypeChoices.TEXT and input_type == Question.InputTypeChoices.NUMBER:
            self._create_number_question(element)

        if question_type == Question.QuestionTypeChoices.TEXT and not input_type:
            self._create_text_question(element)

        if question_type == Question.QuestionTypeChoices.RADIOGROUP:
            self._create_radiogroup_question(element)

        if question_type == Question.QuestionTypeChoices.BOOLEAN:
            self._create_boolean_question(element)

    def _create_date_question(self, element):
        Question.objects.create(
            questionnaire=self.questionnaire_instance,
            question_type=Question.QuestionTypeChoices.TEXT,
            input_type=Question.InputTypeChoices.DATE,
            name=element.get('name'),
            title=element.get('title'),
            subtitle=element.get('description', None)
        )

    def _create_number_question(self, element):
        Question.objects.create(
            questionnaire=self.questionnaire_instance,
            question_type=Question.QuestionTypeChoices.TEXT,
            input_type=Question.InputTypeChoices.NUMBER,
            name=element.get('name'),
            title=element.get('title'),
            subtitle=element.get('description', None)
        )

    def _create_text_question(self, element):
        Question.objects.create(
            questionnaire=self.questionnaire_instance,
            question_type=Question.QuestionTypeChoices.TEXT,
            input_type=Question.InputTypeChoices.TEXT,
            name=element.get('name'),
            title=element.get('title'),
            subtitle=element.get('description', None)
        )

    def _create_radiogroup_question(self, element):
        question = Question.objects.create(
            questionnaire=self.questionnaire_instance,
            question_type=Question.QuestionTypeChoices.RADIOGROUP,
            name=element.get('name'),
            title=element.get('title'),
            subtitle=element.get('description', None)
        )

        choices = element.get('choices', [])
        self._create_radiogroup_option(question, choices)

    @staticmethod
    def _create_radiogroup_option(question, choices):
        for choice in choices:
            Option.objects.create(
                question=question,
                value=choice.get('value'),
                text=choice.get('text'),
            )

    def _create_boolean_question(self, element):
        question = Question.objects.create(
            questionnaire=self.questionnaire_instance,
            question_type=Question.QuestionTypeChoices.BOOLEAN,
            name=element.get('name'),
            title=element.get('title'),
            subtitle=element.get('description', None)
        )

        label_true = element.get('labelTrue', 'بله')
        label_false = element.get('labelFalse', 'خیر')

        self._create_boolean_option(question, label_true, label_false)

    @staticmethod
    def _create_boolean_option(question, label_true, label_false):
        Option.objects.create(
            question=question,
            value="Item 1",
            text=label_true,
        )
        Option.objects.create(
            question=question,
            value="Item 2",
            text=label_false,
        )
