from django.shortcuts import render
from django.views import View

from movies.models import Movie


class MoviesView(View):
    """Список фильмов"""

    def get(self, request):
        movie = Movie.objects.all()
        return render(request, 'movies/movie_list.html', {'movie_list': movie})
