from flask import Flask, request, jsonify
from storage import all_movies, like_movies, dislike_movies, not_watched
from demographic_filtering import output
from Content_filtering import get_recommendations

app = Flask(__name__)
@app.route("/get-movie")
def Get_movie():
    movie_data = {
     "title": all_movies[0][19],
     "poster_link": all_movies[0][27],
     "release_date": all_movies[0][13] or "N/A",
     "duration": all_movies[0][15],
     "rating": all_movies[0][20],
     "overview": all_movies[0][9]
    }
    return jsonify({
        "data": movie_data,
        "status": "successful"
    })

@app.route("/liked-movies", methods = ["POST"])
def like_movies():
    movie = all_movies[0]
    like_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status": "successful"
    }),201

@app.route("/disliked-movies", methods = ["POST"])
def dislike_movie():
    movie = all_movies[0]
    dislike_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status": "successful"
    }),201

@app.route("/unwatched-movies", methods = ["POST"])
def unwatched_movies():
    movie = all_movies[0]
    not_watched.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status": "successful"
    }),201

@app.route("/popular-movies")
def popular_movies():
    movie_data = []
    for movie in output:
            t = {
               "title": movie[0],
               "poster_link": movie[1],
               "release_date": movie[2] or "N/A",
               "runtime": movie[3],
               "vote_average": movie[4],
               "overview": movie[5]
            }
            movie_data.append(t)
    return jsonify({
        "data": movie_data,
        "status": "successful"
    }) ,200

@app.route("/recommended-movies")
def revpommened_movies():
    all_recomended = []
    for i in like_movies:
        output = get_recommendations(i[19])
        for t in output:
            all_recomended.append(t)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    movie_data = []
    for movie in all_recomended:
        t = {
            "title": movie[0],
            "poster_link": movie[1],
            "release_date": movie[2] or "N/A",
            "runtime": movie[3],
            "vote_average": movie[4],
            "overview": movie[5]
            }
        movie_data.append(t)
    return jsonify({
        "data": movie_data,
        "status": "successful"
    }) ,200



if __name__ == "__main__":
  app.run(debug=True)