from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def print_hello(request):
    movie_data = {'movies' : [
        {
        'title' : 'Interstellar',
        'year' : 2012,
        'summary' : 'Story of cooper',
        'sucess' : True
    },
        {
        'title' : 'inception',
        'year' : 2010,
        'summary' : 'Story of cooper',
        'sucess' : True
    },
        {
        'title' : 'Tenat',
        'year' : 2016,
        'summary' : 'Story of cooper',
        'sucess' : False
    },
        {
        'title' : 'Godfather',
        'year' : 1990,
        'summary' : 'Story of cooper',
        'sucess' : False
    },
        {
        'title' : 'Titanic',
        'year' : 2002,
        'summary' : 'Story of cooper',
        'sucess' : True
    },
        {
        'title' : 'Into the wild',
        'year' : 2009,
        'summary' : 'Story of cooper',
        'sucess' : False
    },
        {
        'title' : 'Fight Club',
        'year' : 2007,
        # 'summary' : 'Story of cooper',
        'sucess' : False
    },
        {
        'title' : 'Water',
        'year' : 1998,
        'summary' : 'Story of cooper',
        'sucess' : False
    },
        {
        'title' : 'Gold',
        'year' : 2000,
        'summary' : 'Story of cooper',
        'sucess' : False
    },
        {
        'title' : 'Seven',
        'year' : 2005,
        'summary' : 'Story of cooper',
        'sucess' : False
    },
        {
        'title' : 'The True Man Show',
        'year' : 2001,
        'summary' : 'Story of cooper',
        'sucess' : False
    }
    ]}
    return render(request, "hello.html", movie_data)
    # return HttpResponse("")