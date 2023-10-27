from django.shortcuts import render

from movie_app.models import Movie
from django.shortcuts import render


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)


def Details(request):
    return render(request, 'details.html')
