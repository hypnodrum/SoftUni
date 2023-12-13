import os
import django
from django.db.models import Q, Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Director, Actor, Movie


def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    query = Q()
    query_name = Q(full_name__icontains=search_name)
    query_nationality = Q(nationality__icontains=search_nationality)

    if search_name and search_nationality:
        query = query_name & query_nationality
    elif search_name:
        query = query_name
    else:
        query = query_nationality

    director = Director.objects.filter(query).order_by('full_name')

    if not director:
        return ""

    result = []

    for d in director:
        result.append(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}")

    return "\n".join(result)


def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()

    if not director:
        return ""

    return f"Top Director: {director.full_name}, movies: {director.number_of_movies}."


def get_top_actor():
    top_actor = Actor.objects.annotate(
        number_of_movies = Count('movies'),
        avg_rating = Avg('movies__rating')
    ).order_by('-number_of_movies', 'full_name').first()

    if not top_actor or not top_actor.number_of_movies:
        return ""

    movies = ", ".join([movie.title for movie in top_actor.movies.all() if movie])

    return f"Top Actor: {top_actor.full_name}, starring in movies: {movies}, movies average rating: {top_actor.avg_rating:.1f}"


def get_actors_by_movies_count():
    actors = Actor.objects.annotate(
        num_movies = Count('movie')
    ).order_by('-num_movies', 'full_name')[:3]

    if not actors or not Movie.objects.all():
        return ""

    result = []
    for actor in actors:
        result.append(f"{actor.full_name}, participated in {actor.num_movies} movies")
    return '\n'.join(result)


def get_top_rated_awarded_movie():
    movie = Movie.objects.filter(is_awarded=True).order_by('-rating','title').first()

    if not movie:
        return ""

    starring_actor = movie.starring_actor.full_name if movie.starring_actor else 'N/A'

    cast = []
    for actor in movie.actors.all():
        cast.append(actor.full_name)

    result = (f"Top rated awarded movie: {movie.title}, rating: {movie.rating}. "
              f"Starring actor: {starring_actor}. Cast: {', '.join(cast)}.")
    return result


def increase_rating():
    movies_to_update = Movie.objects.filter(is_classic=True, rating__lt=10)

    if not movies_to_update:
        return "No ratings increased."

    updated_movies = movies_to_update.update(rating=F('rating')+0.1)

    return f"Rating increased for {updated_movies} movies."
