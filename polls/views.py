from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from django.http import HttpResponseRedirect
from .models import Questions
from django.template import loader
from django.urls import reverse
from .models import Choice, Questions
from django.db.models import F
from django.views import generic
from django.utils import timezone

# Create your views here.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name= "latest_question_list"

    def get_queryset(self):
        return Questions.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model = Questions
    template_name = "polls/details.html"
    def get_queryset(self):
        #excludes any questions that are not published yet
        return Questions.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Questions
    template_name = "polls/results.html"

# def index(request):
#     latest_question_list= Questions.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_question_list" : latest_question_list,
#     }
#     return render(request,"polls/index.html", context)

# def details(request, question_id):
#     # try:
#     #     question=Questions.objects.get(pk=question_id)
#     # except Questions.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     question=get_object_or_404(Questions, pk=question_id)
#     return render(request, "polls/detail.html",{'question' : question})


# def results(request, question_id):
#     question=get_object_or_404(Questions, pk=question_id)
#     return render(request,"polls/result.html", {"question":question})
#     #return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        #redisplay the question voting form
        return render(
            request,
            "polls/details.html",
            {
                "question":question,
                "error":"You didnt select a choice.",
            },
        )
    else:
        selected_choice.votes=F("votes")+1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

    return HttpResponse(reverse("polls:results",args=(question.id,)))