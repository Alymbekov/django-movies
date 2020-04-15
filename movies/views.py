from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .forms import ReviewForm

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
