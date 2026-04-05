import requests

API_KEY = "e13a7a6838106ae03166e838a801ef6e"

def get_movie_data(movie_name):
    try:
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
        search = requests.get(search_url).json()

        if len(search['results']) == 0:
            return None

        movie = search['results'][0]
        movie_id = movie['id']

        details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        details = requests.get(details_url).json()

        return {
            "title": details.get("title"),
            "runtime": details.get("runtime", 0),
            "rating": details.get("vote_average", 0),
            "votes": details.get("vote_count", 0),
            "popularity": details.get("popularity", 0),
            "budget": details.get("budget", 0),
            "poster": "https://image.tmdb.org/t/p/w500" + str(details.get("poster_path")) if details.get("poster_path") else ""
        }

    except Exception as e:
        print("Error:", e)
        return None