from django.http import HttpResponse
from .tasks import send_email


def index(request):
    send_email.delay('sadmanhossainridoy@gmail.com')
    return HttpResponse("Hi there!")
