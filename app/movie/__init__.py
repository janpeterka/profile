from app.movie.routes import movie_blueprint


def create_module(app, **kwargs):
    app.register_blueprint(movie_blueprint)
