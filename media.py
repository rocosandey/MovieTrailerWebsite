class Movie(object):

    """Movie class defines a blueprint for a movie. movie_title, image_url, movie_trailer_url needed for constructor"""
    def __init__(self,movie_title,image_url,movie_trailer_url):
        self.title = movie_title
        self.poster_image_url = image_url
        self.trailer_youtube_url = movie_trailer_url