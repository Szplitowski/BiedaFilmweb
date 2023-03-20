import sys, pytest, requests
from unittest.mock import Mock

sys.path.append(r"C:\Users\szpli\Desktop\Projects\movies_project\movies_catalogue")
import tmdb_client
from main import app
from unittest.mock import Mock


@pytest.mark.parametrize(
    "list_type", ["now_playing", "popular", "top_rated", "upcoming"]
)
def test_homepage(monkeypatch, list_type):
    api_mock = Mock(return_value={"results": []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get(f"/?list_type={list_type}")
        assert response.status_code == 200
        api_mock.assert_called_once_with(f"movie/{list_type}")
