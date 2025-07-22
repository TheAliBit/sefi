from django.contrib import admin

from question.models import Question, Questionnaire, Option, Condition, MultiCondition


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    pass


@admin.register(MultiCondition)
class MultiConditionAdmin(admin.ModelAdmin):
    pass
