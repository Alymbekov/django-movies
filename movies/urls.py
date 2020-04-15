from django.urls import path

from . import views


urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("movies/<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("movies/review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
]