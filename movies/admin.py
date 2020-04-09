from django.contrib import admin

from movies.models import Category, Genre, Movie, MovieShots, Actor, Raiting, RatingStar, Reviews

models = [Category, Genre, Movie, MovieShots, Actor, Raiting, RatingStar, Reviews]

for model in models:
    admin.site.register(model)




