from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .forms import ReviewForm

from .models import Movie, Genre, Actor, Genre


class GenreYearMixin():
    """Жанры и года выхода фильмов"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class MoviesView(GenreYearMixin, ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(GenreYearMixin, DetailView):
    """ Полное описание фильма"""
    model = Movie
    slug_field = "url"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['genres'] = Genre.objects.all()
        return context

class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        movie = Movie.objects.get(id=pk)
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie_id = pk 
            form.save()
        return redirect(reverse_lazy("movie_detail", kwargs={"slug": movie.url}))


class ActorView(GenreYearMixin, DetailView):
    """Вывод инфы о актере"""
    model = Actor
    template_name = "movies/actor.html"
    slug_field = "name"


class FilterMoviesView(GenreYearMixin, ListView):
    """Фильтр фильмов"""
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre")) 

        )
        return queryset

class JsonFolterMoviesView(ListView):
    """Фильтр фильмов в json"""
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre")) 
        ).distinct().values("title", "tagline", "url", "poster")
        return queryset
    
    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)
     
    