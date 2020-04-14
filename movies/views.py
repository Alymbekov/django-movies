from django.shortcuts import render
from django.views.generic.base import View


from .models import Movie, Genre


class MoviesView(View):
    """Список фильмов"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movies.html", {"movie_list": movies})


class MovieDetailView(View):
    """ Полное описание фильма"""
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        genres = Genre.objects.all()
        return render(request, "movies/movie_detail.html", {"movie": movie, "genres": genres})