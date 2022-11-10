from app.dao.director import DirectorDAO
from app.dao.genres import GenreDAO
from app.dao.movie import MovieDAO
from app.database import db
from app.services.director import DirectorService
from app.services.genres import GenreService
from app.services.movie import MovieService

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)
