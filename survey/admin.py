from django.contrib import admin
from .models import (SurveyBase, StatisticalGroup, QuestionCatalog,
                     Question, MultipleChoiceAnswerPossibility, QuestionAnswer,
                     Organization, Profile)

# Register your models here.
admin.site.register(SurveyBase)
admin.site.register(StatisticalGroup)
admin.site.register(QuestionCatalog)
admin.site.register(Question)
admin.site.register(MultipleChoiceAnswerPossibility)
admin.site.register(QuestionAnswer)
admin.site.register(Organization)
admin.site.register(Profile)