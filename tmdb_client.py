import requests, json

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMjZhODFmNThmZDI2YWNjMjg5Yjc0YzgyYzFmNGFiMiIsInN1YiI6IjY0MGIzNTE1MzI2ZWMxMDBjNGMwNWQ2NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.piMU7USiMJ1870vadcvmGJyJnJldkVeqzyx2d0_rbnE"


def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_popular_movies():
    return call_tmdb_api(f"movie/popular")


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size.strip()}/{poster_api_path}"


def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]


def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    api_token = API_TOKEN
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)

    if response.status_code != 200:
        raise Exception(response.json().get("status_message", "An error occurred."))

    return response.json()["cast"]


def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")
