from django.http import HttpResponse
from django.shortcuts import render, redirect

from movie_app.forms import MovieForm
from movie_app.models import Movie
from django.shortcuts import render


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)


def Details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "details.html", {'movie': movie})


def Add_Movie(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        short_desc = request.POST.get('short_desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        movie = Movie(name=name, desc=desc, year=year, short_desc=short_desc, img=img)
        movie.save()

    return render(request, 'Add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
        if request.method == "POST":
            movie = Movie.objects.get(id=id)
            movie.delete()
            return redirect('/')
        return render(request, 'delete.html')
