from django.contrib import admin
from .models import Questions, Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]

admin.site.register(Questions, QuestionAdmin)
admin.site.register(Choice)