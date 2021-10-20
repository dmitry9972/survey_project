from django.contrib import admin

from .models import Question, Survey, Survey_result


admin.site.register(Question)
admin.site.register(Survey)
admin.site.register(Survey_result)
