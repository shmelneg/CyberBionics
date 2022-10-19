from django.shortcuts import render
from django.http import HttpResponse, request

def index(request):
    return HttpResponse("<p>Hello World!</p><p>Django є одним з найбільших framework на Python</p><hr>")
