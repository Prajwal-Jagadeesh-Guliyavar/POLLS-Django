from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from .models import Questions
from django.template import loader

# Create your views here.

def index(request):
    latest_question_list= Questions.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list" : latest_question_list,
    }
    return render(request,"polls/index.html", context)

def details(request, question_id):
    # try:
    #     question=Questions.objects.get(pk=question_id)
    # except Questions.DoesNotExist:
    #     raise Http404("Question does not exist")
    question=get_object_or_404(Questions, pk=question_id)
    return render(request, "polls/detail.html",{'question' : question})


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)