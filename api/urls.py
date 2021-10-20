from django.urls import path


from .views import QuestionViewSet, SurveyViewSet, Survey_resultViewSet, \
    ActiveSurveyViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from django.urls import path, include, re_path
from drf_yasg import openapi

from rest_framework import routers

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

router = routers.SimpleRouter()
router.register(r"Question", QuestionViewSet)
router.register(r"QuestionbySurvey/(?P<survey_id>\d+)", QuestionViewSet)
router.register(r"Survey", SurveyViewSet)
router.register(r"ActiveSurvey", ActiveSurveyViewSet)
router.register(r"Survey_result", Survey_resultViewSet)
router.register(r'Survey_resultbyUserandSurvey/(?P<user_id>\d+)/(?P<survey_id>[^/.]+)', Survey_resultViewSet)

urlpatterns += router.urls
