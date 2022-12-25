from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('<h1>  Hello!!!!... </h1>')

def second(request):
    return HttpResponse('<marquee><h1>Welcome to the Page!!!!... <h1></marquee> ')

def third(request):
    return HttpResponse(' My first task!!.. ')
