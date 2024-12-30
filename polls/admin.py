from django.contrib import admin
from .models import Questions, Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Details", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

admin.site.register(Questions, QuestionAdmin)
admin.site.register(Choice)