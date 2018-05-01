# -*- coding: utf-8 -*-
"""Media module

This module includes a class for movies.
"""


class Movie(object):
    """A movie class with title, image and trailer.

    Attributes:
        title               The title of the movie
        poster_image_url    The link to the poster image on the web
        trailer_youtube_url The link to the trailer on Youtube

    Example:
        The movie class can be instantiate as in the following example
        pulp_fiction = Movie("Pulp Fiction",
                     "https://pics.filmaffinity.com/"
                     "Pulp_Fiction-210382116-large.jpg",
                     "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

    """

    def __init__(self, movie_title, image_url, movie_trailer_url):
        self.title = movie_title
        self.poster_image_url = image_url
        self.trailer_youtube_url = movie_trailer_url
