from django.shortcuts import render

# Create your views here.


def create(request):
    if request.POST:
        print(request.POST)
        print(request.POST.get('title'))
        print(request.POST.get('year'))
        print(request.POST.get('summary'))
    return render(request, 'create.html')


def list(request):
    movie_data = {'movies' : [
            {
            'title' : 'Interstellar',
            'year' : 2012,
            'summary' : 'Story of cooper',
            'sucess' : True,
            'img' : 'interstellar.jpg'
        },
            {
            'title' : 'inception',
            'year' : 2010,
            'summary' : 'Story of cooper',
            'sucess' : True,
            'img' : 'inception.jpg'

        },
            {
            'title' : 'Tenat',
            'year' : 2016,
            'summary' : 'Story of cooper',
            'sucess' : False,
            'img' : 'tenet.jpg'
        },
            {
            'title' : 'Godfather',
            'year' : 1990,
            'summary' : 'Story of cooper',
            'sucess' : False,
            'img' : 'godfather.jpg'

        },
            {
            'title' : 'Titanic',
            'year' : 2002,
            'summary' : 'Story of cooper',
            'sucess' : True,
            'img' : 'titanic.jpg'
        },
            {
            'title' : 'Into the wild',
            'year' : 2009,
            'summary' : 'Story of cooper',
            'sucess' : False,
            'img' : 'into the wild.jpg'
        },
            {
            'title' : 'Fight Club',
            'year' : 2007,
            # 'summary' : 'Story of cooper',
            'sucess' : False,
            'img' : 'fight club.jpg'
        },
            {
            'title' : 'Water',
            'year' : 1998,
            'summary' : 'Story of cooper',
            'sucess' : False,
            'img' : 'titanic.jpg'
        },
            {
            'title' : 'Gold',
            'year' : 2000,
            'summary' : 'Story of cooper',
            'sucess' : False,
            'img' : 'godfather.jpg'
        },
            {
            'title' : 'Seven',
            'year' : 2005,
            'summary' : 'Story of cooper',
            'sucess' : False,
            'img' : 'seven.jpg'
        },
            {
            'title' : 'The True Man Show',
            'year' : 2001,
            'summary' : 'Story of cooper',
            'sucess' : False,
            'img' : 'the true man show.jpg'
        }
    ]}
    return render(request, 'list.html', movie_data)

def edit(request):
    return render(request, 'edit.html')