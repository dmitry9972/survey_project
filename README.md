Full development log:  
survey_project/development_log.odt   


How to install:  
mkdir survey_project  
cd survey_project  
pip install virtualenv  
virtualenv newenv  
source newenv/bin/activate  
pip install django==2.2.10  
pip install djangorestframework==3.12.4  
pip install django-cors-headers
pip install -U drf-yasg
git clone https://github.com/dmitry9972/survey_project.git
cd survey_project
python3 manage.py runserver


API Documentation:
http://127.0.0.1:8000/api/swagger/
http://127.0.0.1:8000/api/redoc/


Curl-request examples:

Making survey:
curl -X POST -H "Authorization: Token 80e5926c35fd17acf3fa2d6b75ee2d84b0135de8" -d "name='TEST SURVEY 333'&description='CURL TEST SURVEY333'&start_date=29-10-2021 14-36-23&end_date=29-10-2022 14-36-23" 'http://127.0.0.1:8000/api/Survey/'
response:{"id":5,"name":"'TEST SURVEY 333'","description":"'CURL TEST SURVEY333'","start_date":"2021-10-19T14:36:23Z","end_date":"2022-10-29T14:36:23Z"}

Making survey questions:
curl -X POST -H "Authorization: Token 80e5926c35fd17acf3fa2d6b75ee2d84b0135de8" -d "text=Тест вопрос 1?&type=1&answer_options=null&survey=5" 'http://127.0.0.1:8000/api/Question/'
response: {"id":5,"text":"Тест вопрос 1?","type":1,"answer_options":"null","survey":5}

Making survey questions:
curl -X POST -H "Authorization: Token 80e5926c35fd17acf3fa2d6b75ee2d84b0135de8" -d "text=Тест вопрос 2?&type=1&answer_options=null&survey=5" 'http://127.0.0.1:8000/api/Question/'

What surveys are active now?
curl -X GET 'http://127.0.0.1:8000/api/ActiveSurvey/'

Number of questions in survey?
curl -X GET 'http://127.0.0.1:8000/api/ActiveSurvey/5/'

Getting survey questions by survey_id:
curl -X GET 'http://127.0.0.1:8000/api/QuestionbySurvey/5/'

Answering first question:
curl -X POST -d "user=1&answer="\"ДА\",\"НАВЕРНОЕ\""&survey=5&question=5" 'http://127.0.0.1:8000/api/Survey_result/'
or
curl -X POST -d "user=1&answer="\"ДА\",\"НАВЕРНОЕ\""&survey=5&question=5" 'http://127.0.0.1:8000/api/Survey_resultbyUserandSurvey/1/5/'

Answering second question:
curl -X POST -d "user=1&answer="\"ДА\""&survey=5&question=6" 'http://127.0.0.1:8000/api/Survey_result/'
response:{"id":10,"user":1,"answer":"\"ДА\"","survey":5,"question":6}

Getting survey results:
curl -X GET 'http://127.0.0.1:8000/api/Survey_resultbyUserandSurvey/1/5/'




