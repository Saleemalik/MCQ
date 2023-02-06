from django.contrib import admin
from django.contrib.auth.models import User
from . models import MCQ, Answer

# Register your models here.
admin.site.register(MCQ)
admin.site.register(Answer)
