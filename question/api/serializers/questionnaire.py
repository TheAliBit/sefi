from rest_framework import serializers

from question.models import Questionnaire


class CreateQuestionnaireFromJsonSerializer(serializers.Serializer):
    form = serializers.JSONField()
