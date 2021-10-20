from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from main.models import Question, Survey, Survey_result
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, UpdateAPIView
from .serializers import QuestionSerializer, SurveySerializer, \
    ActiveSurveySerializer, Survey_resultSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import viewsets
from datetime import datetime
from .permissions import AdminPermission


class UserSurveyViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)


class AdminSurveyViewSet(viewsets.ModelViewSet):
    permission_classes = (AdminPermission,)


class QuestionViewSet(AdminSurveyViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get_queryset(self):

        if 'survey_id' in self.kwargs:
            survey_id = self.kwargs['survey_id']
            return Question.objects.filter(survey__id=survey_id)
        else:
            return Question.objects.all()



class SurveyViewSet(AdminSurveyViewSet):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()



class ActiveSurveyViewSet(AdminSurveyViewSet):
    serializer_class = ActiveSurveySerializer
    queryset = Survey.objects.filter(end_date__gte=datetime.now(), start_date__lte=datetime.now())


class Survey_resultViewSet(UserSurveyViewSet):
    serializer_class = Survey_resultSerializer
    queryset = Survey_result.objects.all()

    def get_queryset(self):

        if 'user_id' in self.kwargs and 'survey_id' in self.kwargs:
            user_id = self.kwargs['user_id']
            survey_id = self.kwargs['survey_id']
            return Survey_result.objects.filter(user=user_id, survey__id=survey_id)
        else:
            return Survey_result.objects.all()
