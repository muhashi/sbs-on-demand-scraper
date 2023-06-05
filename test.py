from script import get_num_movies, scrape


def validate_movie(movie: dict):
    assert isinstance(movie.get("id"), str)
    assert isinstance(movie.get("entityType"), str)
    assert isinstance(movie.get("title"), str)
    assert isinstance(movie.get("slug"), str)
    assert isinstance(movie.get("description"), str)
    assert isinstance(movie.get("genres"), list)
    assert isinstance(movie.get("languages"), list)
    assert isinstance(movie.get("textTracks"), list)
    assert isinstance(movie.get("availability"), dict)
    assert isinstance(movie.get("hasAudioDescription"), bool)
    assert isinstance(movie.get("classificationID"), str)
    assert isinstance(movie.get("images"), list)
    assert isinstance(movie.get("distributors"), list)
    assert isinstance(movie.get("duration"), str)
    assert isinstance(movie.get("mpxMediaID"), int)
    assert isinstance(movie.get("releaseYear"), int)
    
    assert len(movie) == 16

def test_get_num_movies():
    num_movies = get_num_movies()
    default_value = 1000

    assert num_movies != default_value
    assert num_movies > 0

def test_scrape_one_page():
    movies = scrape(max_pages=1)

    assert len(movies) == 100

    ids = set()
    descriptions = set()

    for movie in movies:
        validate_movie(movie)
        assert movie.get("id") not in ids
        assert movie.get("description") not in descriptions

        ids.add(movie.get("id"))
        descriptions.add(movie.get("description"))

def test_scrape_all_pages():
    movies = scrape()

    assert len(movies) > 100

    ids = set()
    descriptions = set()

    for movie in movies:
        validate_movie(movie)

        assert movie.get("id") not in ids
        assert movie.get("description") not in descriptions

        ids.add(movie.get("id"))
        descriptions.add(movie.get("description"))
