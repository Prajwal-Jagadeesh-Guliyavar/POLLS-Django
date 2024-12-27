from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # URL pattern for the index page (list of questions)
    path("", views.IndexView.as_view(), name="index"),

    # URL pattern for viewing a single question's details
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    # URL pattern for viewing the results of a question
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),

    # URL pattern for voting on a question
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
