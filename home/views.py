from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, world. You're at the home page.</h1>"
                        "<p>This is the home page.</p>")