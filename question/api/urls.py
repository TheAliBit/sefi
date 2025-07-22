from django.urls import path
from rest_framework.routers import DefaultRouter

from question.api.views.questionnaire import QuestionnaireViewSet

router = DefaultRouter()

router.register('create', QuestionnaireViewSet)

urlpatterns = [

              ] + router.urls
