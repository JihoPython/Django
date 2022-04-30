from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld


def hello_world(request: HttpRequest):
    if request.method == 'POST':
        message = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = message
        new_hello_world.save()

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})

    return render(request, 'accountapp/hello_world.html')
