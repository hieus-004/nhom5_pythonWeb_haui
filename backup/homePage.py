from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the tech_part index.")

def homePage(request):
    return render(request, 'homePage.html')

