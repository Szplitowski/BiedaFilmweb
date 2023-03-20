import sys, pytest, requests
from requests.exceptions import HTTPError
from unittest.mock import Mock

sys.path.append(r"C:\Users\szpli\Desktop\Projects\movies_project\movies_catalogue")
import tmdb_client


# skopiowane z kursu


def test_get_poster_url_uses_default_size():
    poster_api_path = "some-poster-path"
    expected_default_size = "w342"
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    assert expected_default_size in poster_url


def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list is not None


def test_get_movies_list(monkeypatch):
    mock_movies_list = ["Movie 1", "Movie 2"]
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list

    # /skopiowane z kursu


def test_get_single_movie():
    movie_id = 550
    result = tmdb_client.get_single_movie(movie_id)
    assert result["id"] == movie_id


def test_get_single_movie_cast_endpoint(monkeypatch):
    class MockResponse:
        def __init__(self):
            self.status_code = 200

        def json(self):
            return {"cast": [{"name": "Actor 1"}, {"name": "Actor 2"}]}

    def mock_get(*args, **kwargs):
        assert args[0] == "https://api.themoviedb.org/3/movie/550/credits"
        return MockResponse()

    monkeypatch.setattr("tmdb_client.requests.get", mock_get)
    movie_id = 550
    result = tmdb_client.get_single_movie_cast(movie_id)


def test_get_single_movie_cast_error_handling(monkeypatch):
    class MockResponse:
        def __init__(self):
            self.status_code = 404

        def json(self):
            return {"status_message": "Id is invalid or not found."}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("tmdb_client.requests.get", mock_get)
    movie_id = 550
    with pytest.raises(Exception) as e:
        result = tmdb_client.get_single_movie_cast(movie_id)

    assert str(e.value) == "Id is invalid or not found."


def test_get_popular_movies():
    mock_response = Mock()
    mock_response.json.return_value = {"results": ["Movie 1", "Movie 2"]}
    requests.get = Mock(return_value=mock_response)
    response = tmdb_client.get_popular_movies()
    assert response == {"results": ["Movie 1", "Movie 2"]}
