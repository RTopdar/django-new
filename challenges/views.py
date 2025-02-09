from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


challenges = [
    {
        "month": "january",
        "title": "January Challenge: Eat no meat for the entire month",
    },
    {
        "month": "february",
        "title": "February Challenge: Walk for at least 20 minutes every day",
    },
    {
        "month": "march",
        "title": "March Challenge: Read a book for at least 30 minutes every day",
    },
    {
        "month": "april",
        "title": "April Challenge: Practice meditation for 10 minutes every day",
    },
    {
        "month": "may",
        "title": "May Challenge: Write a journal entry every day",
    },
    {
        "month": "june",
        "title": "June Challenge: Learn a new word and use it in a sentence every day",
    },
    {
        "month": "july",
        "title": "July Challenge: Drink at least 8 glasses of water every day",
    },
    {
        "month": "august",
        "title": "August Challenge: Exercise for at least 30 minutes every day",
    },
    {
        "month": "september",
        "title": "September Challenge: Cook a new recipe every week",
    },
    {
        "month": "october",
        "title": "October Challenge: Take a photo of something that makes you happy every day",
    },
    {
        "month": "november",
        "title": "November Challenge: Write a thank-you note to someone every week",
    },
    {
        "month": "december",
        "title": "December Challenge: Reflect on your goals and set new ones for the next year",
    },
]


def index(request):
    return HttpResponse(f"This works! {request}")


def view_month_wise_challenge(request, month):
    challenge_text = None
    for challenge in challenges:
        if challenge["month"] == month:
            challenge_text = challenge["title"]
            break
    if challenge_text is None:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)


def view_number_wise_challenge(request, number):
    try:
        redirect_to = challenges[number - 1]["month"]
        redirect_path = reverse("month-challenge", args=[redirect_to])
        print(redirect_path)
        return HttpResponseRedirect(f"/challenges/{redirect_to}")
    except IndexError:
        return HttpResponseNotFound("This number is not supported!")
