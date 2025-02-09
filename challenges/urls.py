from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("<int:number>", views.view_number_wise_challenge),
    path("<str:month>", views.view_month_wise_challenge, name="month-challenge"),
]
