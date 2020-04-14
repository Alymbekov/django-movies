from django.shortcuts import render
from django.views.generic import ListView, DetailView


from .models import Movie, Genre


class MoviesView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """ Полное описание фильма"""
    model = Movie
    slug_field = "url"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['genres'] = Genre.objects.all()
        return context

