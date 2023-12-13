from django.db import models


class DirectorManager(models.Manager):
    def get_directors_by_movies_count(self):
        return self.annotate(
            number_of_movies = models.Count('movies')).order_by('-number_of_movies', 'full_name')

