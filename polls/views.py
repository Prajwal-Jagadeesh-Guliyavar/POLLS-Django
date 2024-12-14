from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions
from django.template import loader

# Create your views here.

def index(request):
    latest_question_list= Questions.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list" : latest_question_list,
    }
    return HttpResponse(request,"polls/index.html", context)

def details(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)