# Generated by Django 2.2.10 on 2021-10-20 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_question_answer_options'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='survey_result',
            unique_together={('user', 'survey', 'question')},
        ),
    ]