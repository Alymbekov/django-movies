from django.contrib import admin

from movies.models import Category, Genre, Movie, MovieShots, Actor, Raiting, RatingStar, Reviews

# models = [Category, Genre, Movie, MovieShots, Actor, Raiting, RatingStar, Reviews]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории фильмов"""
    list_display = ("id","name", "url")
    list_display_links = ("name", )


class ReviewInline(admin.TabularInline):
    """Отзывы на странице фильма"""
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ("title", "category", "url", "draft", )
    list_filter = ("category", "year", )
    search_fields = ("title", "category__name", )
    inlines  = [ReviewInline, ]
    save_on_top = True
    save_as = True 
    list_editable = ("draft", )
    # fields = (("actors", "directors", "genres"), )
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", "poster",)
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"),)
        }),
        ("Actors", {
            "classes": ("collapse", ),
            "fields": (("actors", "directors", "genres", "category"), )
        }),
        (None, {
            "fields": (("budget", "fess_in_world"), )
        }),
        ("Options", {
            "fields": (("url", "draft"), )
        }),
    )
    

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id", )
    readonly_fields = ("name", "email", )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ("name", "url") 


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актеры"""
    list_display = ("name", "age", "description")


@admin.register(Raiting)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("ip", "movie")


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ("title", "movie")


# admin.site.register(Category, CategoryAdmin)

# for model in models:
#     admin.site.register(model)




