from django.http import HttpRequest, HttpResponse


def hello_world(request: HttpRequest):
    return HttpResponse('Hello World!')
