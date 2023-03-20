import requests, json

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMjZhODFmNThmZDI2YWNjMjg5Yjc0YzgyYzFmNGFiMiIsInN1YiI6IjY0MGIzNTE1MzI2ZWMxMDBjNGMwNWQ2NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.piMU7USiMJ1870vadcvmGJyJnJldkVeqzyx2d0_rbnE"


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = API_TOKEN
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()


response = get_popular_movies()
movies = response["results"]
# for movie in movies:
#    print(movie["title"])


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size.strip()}/{poster_api_path}"


def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_token = API_TOKEN
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    api_token = API_TOKEN
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

    if response.status_code != 200:
        raise Exception(response.json().get("status_message", "An error occurred."))
    return response.json()["cast"]


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type.strip()}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()
