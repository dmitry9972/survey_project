from rest_framework import serializers
from main.models import Question, Survey, Survey_result


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('__all__')


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('__all__')


class ActiveSurveySerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField('get_questions_count')

    def get_questions_count(self, obj):
        questions_count = Question.objects.filter(survey__pk=obj.pk).count()
        return questions_count

    class Meta:
        model = Survey
        fields = ('questions_count', 'name', 'description', 'start_date', 'end_date')


class Survey_resultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey_result
        fields = ('__all__')
