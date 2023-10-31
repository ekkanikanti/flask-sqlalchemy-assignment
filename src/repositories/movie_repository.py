class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        return self.query.all()

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        return self.query.get(movie_id)

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        return self.session.add(title, director, rating)

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return self.query.filter(self.message.match(title)).all()


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
