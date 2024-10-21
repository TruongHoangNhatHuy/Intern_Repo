from django.http import HttpResponse, Http404
from django.template import loader
from polls.models import Question

# helper function for loose coupling
from django.shortcuts import render, get_object_or_404, get_list_or_404


def index(request):
    # short-hand: render()
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
    # standard
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    # short-hand: get_object_or_404()
    q = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": q})
    # standard
    try:
        q = Question.objects.get(pk=question_id)
        return render(request, "polls/detail.html", {"question": q})
    except Question.DoesNotExist:
        raise Http404("Question does not exist")


def results(request, question_id):
    response = "You're lokking at the result of question %s"
    return HttpResponse(response %question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" %question_id)