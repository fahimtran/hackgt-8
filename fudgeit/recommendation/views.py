from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, '../templates/home_page.html')


def questionnaire(request):
    return render(request, '../templates/questionnaire.html')


def recommendations(request):
    return render(request, '../templates/recommendations.html')

