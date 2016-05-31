import webbrowser

class Movie():

        """

        This Class includes property and method that help
        to build the library website

        """
        VALID_RATINGS = ["G", "PG", "PG-13", "R"]
        def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube

        # the following method help to open a specific trailer
        def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)
