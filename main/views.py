import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

'''def home(request):
    print('http://127.0.0.1:8000/main/VSCode')
    return HttpResponse("Hello, Django!")'''

def hello_there(request, name):
    return render(
        request,
        'main/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def home(request):
    return render(request, "main/home.html")

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")