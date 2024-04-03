from django.shortcuts import render
from django.http import HttpResponse
import json
from .responses import bot_response
from .responses import reset_last_message

# Create your views here.

def backend(request, slug=None):
    return HttpResponse("<p>Hello from the backend-side</p>")

def get_chat_response(request, slug=None):
    data = request.GET
    message = data.get("message")

    response = {
        "message": bot_response(message)
    }

    return HttpResponse(json.dumps(response))

def get_first_message(request, slug=None):
    reset_last_message()
    response = {
        "message": "Hello there!"
    }

    return HttpResponse(json.dumps(response))


