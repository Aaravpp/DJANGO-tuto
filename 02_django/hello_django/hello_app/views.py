from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def print_hello(request):
    movie_details = {
        'title' : 'Interstellar',
        'year' : 2012,
        'summary' : 'Story of cooper',
        'sucess' : False
    }
    return render(request, "hello.html", movie_details)
    # return HttpResponse("")