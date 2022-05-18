import http.server
import socketserver
import os
import json
import threading
import requests

#PORT = 8000
#
#web_dir = os.path.join(os.path.dirname(__file__), 'D:/Users/Taylor/Desktop')
#os.chdir(web_dir)
#
#Handler = http.server.SimpleHTTPRequestHandler
#httpd = socketserver.TCPServer(("", PORT), Handler)
#print("serving at port", PORT)
#httpd.serve_forever()

api_key = '9ba37aca04338a3886c632201a0a7dce'
Movie_search = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query="
Genre = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
Test_movie = "Star Wars Episode 07 (2015) The Force Awakens"

class Movie:
    
    def __init__(self, json):
        super().__init__()
        self.genres = json["genre_ids"]
        self.movie_id = json["id"]
        self.title = json["original_title"]
        self.overview = json["overview"]
        self.popularity = json["popularity"]
        self.poster = json["poster_path"]
        self.release_date = json["release_date"]


    def add_title(self):
        pass

    def get_details(self):
        pass

    def __str__(self):
        pass

class TV_episode:
    
    def __init__(self, json):
        super().__init__()

    def add_season(self, id):
        pass

    def add_edisode(self, id):
        pass

    def get_details(self):
        pass

    def __str__(self):
        pass

class TV_Show:
    
    def __init__(self, json):
        super().__init__()

    def add_title(self, id):
        pass

    def get_details(self):
        pass

    def __str__(self):
        pass


class Searched_request(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url
        self.response = {}
        self.listed_results = []

    def run(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            movies_returned = response.json()
            self.listed_results = movies_returned["results"]
            if len(self.listed_results) < 1:
                print("No results found")
            else:
                self.response = self.listed_results[0]
        else:
            print("Error retrieveing data on ",self.url)

class API_request(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url
        self.response = {}

    def run(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.response = response.json()
        else:
            print("Error retrieveing data on ",self.url)

def get_movie(name,movie_file):
    url = Movie_search + name
    json = Searched_request(url)
    json.start()
    json.join()
    if len(json.response) == 0:
        movie = f"The movie file {name} couldnt be found. Make sure the filename is labled as simply the movie title"
    else:
        movie = Movie(json.response)
    return movie

def get_tv_show(name,tv_file):
    #url = TV_search + name
    pass

def get_trending():
    trend_m_url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={api_key}"
    call_m = API_request(trend_m_url)

    trend_t_url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={api_key}"
    call_tv = API_request(trend_t_url)

    call_m.start()
    call_tv.start()

    call_m.join()
    call_tv.join() 

    return call_m.response, call_tv.response

def get_genre_list():
    genres_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
    genre_list = API_request(genres_url)
    genre_list.start()
    genre_list.join()

    return genre_list.response["genres"]

def main():
    movie_data = get_movie(Test_movie,Test_movie)
    genre_list = get_genre_list()

    print(movie_data.title)
    print(movie_data.overview)

    print(genre_list)


if __name__ == "__main__":
    main()