"""
Base Models for creating surveys.
Includes:
    -
    -
    -
"""
import datetime
from django.db import models
from .org_models import Organization, Profile
from ..util.validators import AGE_GROUP_VALIDATORS, IS_NOT_NEGATIVE_VALIDATOR


class SurveyBase(models.Model):
    """
    SurveyBase provides the construct for creating surveys.
    """
    survey_title = models.CharField(max_length=255, blank=False, null=False)
    survey_description = models.CharField(max_length=1023, blank=False, null=False)
    survey_owner_org = models.ForeignKey(to=Organization, on_delete=models.CASCADE, blank=False, null=False)
    survey_owner_user = models.ForeignKey(to=Profile, on_delete=models.PROTECT, blank=False, null=False)
    survey_approval_required = models.BooleanField()
    survey_due_date = models.DateField()
    survey_creation_date = models.DateField(default=datetime.date.today)
    survey_archived = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Survey Bases"
        verbose_name = "Survey Basis"


class StatisticalGroup(models.Model):
    """
    Group for classifying answers given.
    """
    group_name = models.CharField(max_length=255, blank=False, null=False)
    group_description = models.CharField(max_length=1023, blank=False, null=False)
    group_age_lower_bound = models.IntegerField(default=0, validators=AGE_GROUP_VALIDATORS)
    group_age_upper_bound = models.IntegerField(default=100, validators=AGE_GROUP_VALIDATORS)
    group_target_size = models.IntegerField(default=100, null=True, blank=True, validators=IS_NOT_NEGATIVE_VALIDATOR)

    class Meta:
            verbose_name_plural = "Statistical Groups"

class QuestionCatalog(models.Model):
    """
    Question Catalogs encapsulate questions to provide ownership details
    and classification.
    """
    question_catalog_org = models.ForeignKey(to=Organization, on_delete=models.CASCADE)
    question_catalog_name = models.CharField(max_length=255, blank=False, null=False)
    question_catalog_description = models.CharField(max_length=1023, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Question Catalogs"


class Question(models.Model):
    """
    Questions are the survey's main component.
    """
    question_title = models.CharField(max_length=255, blank=False, null=False)
    question_is_multiple_choice = models.BooleanField(default=False, null=False, blank=False)
    # if it is multiple choice, answers can be selected
    question_is_numeric = models.BooleanField(default=False, null=False, blank=False)
    # if it is numeric, provide the allowed range
    question_numeric_range_upper_bound = models.IntegerField(blank=True, null=True)
    question_numeric_range_lower_bound = models.IntegerField(blank=True, null=True)
    # if it is none of the above, answer is free text


class MultipleChoiceAnswerPossibility(models.Model):
    """
    Answer possibilities for multiple choice questions.
    """
    related_question = models.ManyToManyField(to=Question)
    answer_text = models.CharField(max_length=1023, blank=False, null=False)
    answer_comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Multiple Choice Answer Possbilities"


class QuestionAnswer(models.Model):
    """
    Question Answer for free text questions
    """
    related_question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1023, blank=False, null=False)
    answer_comment = models.CharField(max_length=255, blank=True, null=True)
    answer_date = models.DateTimeField(default=datetime.datetime.now)
    answer_stat_group = models.ForeignKey(StatisticalGroup, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Question Answers"
        verbose_name = "Question Answer"

