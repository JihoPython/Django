from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def hello_world(request: HttpRequest):
    return render(request, 'base.html')
