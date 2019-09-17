from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Organization, SurveyBase


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class SurveyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyBase
        fields = ('survey_title', 'survey_description', 'survey_approval_required',
                  'survey_due_date', 'survey_creation_date', 'survey_archived')

    def create(self, validated_data):
        return SurveyBase.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.survey_title = validated_data.get(
            'survey_title', instance.survey_title)
        instance.survey_description = validated_data.get(
            'survey_description', instance.survey_description)
        instance.survey_approval_required = validated_data.get(
            'survey_approval_required', instance.survey_approval_required)
        instance.survey_due_date = validated_data.get(
            'survey_due_date', instance.survey_due_date)
        instance.survey_archived = validated_data.get(
            'survey_archived', instance.survey_archived)
        instance.save()
        return instance
