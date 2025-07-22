from celery import shared_task
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet

from question.api.serializers.questionnaire import CreateQuestionnaireFromJsonSerializer
from question.models import Questionnaire
from question.tasks import Builder


@shared_task
def build_questionnaire(survey_json):
    builder = Builder(survey_json=survey_json)
    builder.build()


class QuestionnaireViewSet(mixins.CreateModelMixin,
                           GenericViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = CreateQuestionnaireFromJsonSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        survey_json = serializer.data.get('form')
        build_questionnaire.delay(survey_json=survey_json)

        return Response(data={"Survey creation started successfully"}, status=status.HTTP_202_ACCEPTED)
