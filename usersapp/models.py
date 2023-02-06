from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MCQ(models.Model):
    question = models.CharField(max_length=255)
    choice_1 = models.CharField(max_length=100, blank=True, null=True)
    choice_2 = models.CharField(max_length=100, blank=True, null=True)
    choice_3 = models.CharField(max_length=100, blank=True, null=True)
    choice_4 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.question

    

class Answer(models.Model):
    student =  models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(MCQ, on_delete=models.DO_NOTHING)
    choices = (
        ('choice_1', 'choice_1'),
        ('choice_2', 'choice_2'),
        ('choice_3', 'choice_3'),
        ('choice_4', 'choice_4'),
    )
    answer = models.CharField(max_length=50, choices=choices, blank=True, null=True)

    class Meta:
        unique_together = ('student', 'question')

    def __str__(self):
        return '%s - %s' % (self.student, self.question)