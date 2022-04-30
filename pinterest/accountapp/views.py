from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def hello_world(request: HttpRequest):
    if request.method == 'POST':
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD!'})

    return render(request, 'accountapp/hello_world.html')
