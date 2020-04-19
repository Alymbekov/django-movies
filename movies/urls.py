from django.urls import path

from . import views


urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("movies/<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("movies/review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("filter/", views.FilterMoviesView.as_view(), name="filter"),
    path("json-filter/", views.JsonFolterMoviesView.as_view(), name="json_filter"),
    path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
]