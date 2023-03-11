from flask import Flask, render_template, request
import tmdb_client

app = Flask(__name__)


@app.route("/")
def homepage():
    available_lists = ["now_playing", "popular", "top_rated", "upcoming"]
    selected_list = request.args.get("list_type", "popular")
    if selected_list not in available_lists:
        selected_list = "popular"
    movies = tmdb_client.get_movies_list(list_type=selected_list)["results"][:8]
    return render_template(
        "homepage.html",
        movies=movies,
        current_list=selected_list,
        available_lists=available_lists,
    )


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)

    return {"tmdb_image_url": tmdb_image_url}


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=details, cast=cast)


if __name__ == "__main__":
    app.run(debug=True)
