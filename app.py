from flask import Flask

app = Flask(__name__)

movies = {
    "M101": {
        "title": "Salaar",
        "director": "Prashanth Neel",
        "language": "Telugu",
        "genre": "Action",
        "rating": 8,
        "year": 2023
    },

    "M102": {
        "title": "Mirchi",
        "director": "Koratala Siva",
        "language": "Telugu",
        "genre": "Action",
        "rating": 7,
        "year": 2013
    },

    "M103": {
        "title": "Bahubali",
        "director": "S. S. Rajamouli",
        "language": "Telugu",
        "genre": "Action",
        "rating": 9,
        "year": 2015
    },

    "M104": {
        "title": "Darling",
        "director": "A. Karunakaran",
        "language": "Telugu",
        "genre": "Romance",
        "rating": 8,
        "year": 2010
    },

    "M105": {
        "title": "Raghuvaran B.Tech",
        "director": "Velraj",
        "language": "Tamil",
        "genre": "Drama",
        "rating": 8,
        "year": 2014
    },

    "M106": {
        "title": "Lucky Baskhar",
        "director": "Venky Atluri",
        "language": "Telugu",
        "genre": "Crime",
        "rating": 8,
        "year": 2024
    }
}


@app.route('/')
def home():
    return "Welcome to Movie Finder"


@app.route('/movies')
def all_movies():
    return movies


@app.route('/movies/id=<string:movie_id>')
def get_movie(movie_id):
    if movie_id in movies:
        return movies[movie_id]

    return "Movie not found"


@app.route('/movies/director=<string:director_name>')
def movie_director(director_name):
    result = []

    for movie in movies.values():
        if movie["director"].lower() == director_name.lower():
            result.append(movie)

    if result:
        return result

    return "No movies found"


@app.route('/movies/rating=<int:rating_no>')
def movie_rating(rating_no):
    result = []

    for movie in movies.values():
        if movie["rating"] == rating_no:
            result.append(movie)

    if result:
        return result

    return "No movies found"


@app.route('/movies/language=<string:language>')
def movie_language(language):
    result = []

    for movie in movies.values():
        if movie["language"].lower() == language.lower():
            result.append(movie)

    if result:
        return result

    return "No movies found"


@app.route('/movies/genre=<string:genre>')
def movies_genre(genre):
    result = []

    for movie in movies.values():
        if movie["genre"].lower() == genre.lower():
            result.append(movie)

    if result:
        return result

    return "No movies found"


@app.route('/movies/year=<int:year>')
def movies_year(year):
    result = []

    for movie in movies.values():
        if movie["year"] == year:
            result.append(movie)

    if result:
        return result

    return "No movies found for this year"


@app.route('/movies/language=<string:language>/genre=<string:genre>')
def language_genre(language, genre):
    result = []

    for movie in movies.values():
        if (movie["language"].lower() == language.lower()
                and movie["genre"].lower() == genre.lower()):
            result.append(movie)

    if result:
        return result

    return "No movies found"


if __name__ == '__main__':
    app.run(debug=True)