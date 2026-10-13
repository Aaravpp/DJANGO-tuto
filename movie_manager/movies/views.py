from django.shortcuts import render
from .  models import MovieInfo
from . forms import MovieFrom

# Create your views here.


def create(request):
    frm = MovieFrom()
    if request.POST:
        # print(request.POST)
        title = request.POST.get('title')
        year = request.POST.get('year')
        description = request.POST.get('summary')
        movie_obj = MovieInfo(title = title, year = year, description = description)
        movie_obj.save()

    return render(request, 'create.html', {'frm' : frm})


def list(request):
    movie_set = MovieInfo.objects.all()
    print(movie_set)
    return render(request, 'list.html', {'movies': movie_set})

def edit(request):
    return render(request, 'edit.html')